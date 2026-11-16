"""Prueba sin servicio MongoDB de la generación de reportes a partir de un adaptador sintético.

No reemplaza la prueba integrada del pipeline contra MongoDB en el equipo destino.
"""
import importlib.util
import sys
import types
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ColeccionSimulada:
    def __init__(self, docs):
        self.docs = docs

    def aggregate(self, pipeline, maxTimeMS=None):
        if any("$project" in stage and "cve_ent" in stage["$project"] for stage in pipeline):
            out = []
            for d in self.docs:
                out.append({
                    "_id": d["_id"],
                    "cve_ent": d["territorio"]["cve_ent"],
                    "tamloc": d["territorio"]["tamloc"],
                    "tamloc_descripcion": d["territorio"]["tamloc_descripcion"],
                    "registros_microdato": d["conteos"]["registros_microdato"],
                    "poblacion_ponderada": d["conteos"]["poblacion_ponderada"],
                    **d["indicadores"],
                })
            return out
        if any("$group" in stage and "media_no_ponderada_de_dominios" in stage["$group"] for stage in pipeline):
            por_tamano = {}
            for d in self.docs:
                key = d["territorio"]["tamloc"]
                por_tamano.setdefault(key, []).append(d["indicadores"]["escolaridad_promedio"])
            return [
                {"_id": key, "dominios_validos": len(val), "media_no_ponderada_de_dominios": sum(val) / len(val),
                 "min": min(val), "max": max(val)}
                for key, val in sorted(por_tamano.items())
            ]
        if any("$group" in stage and "registros_microdato" in stage["$group"] for stage in pipeline):
            por_tamano = {}
            for d in self.docs:
                key = d["territorio"]["tamloc"]
                rec = por_tamano.setdefault(key, {"_id": key, "dominios": 0,
                                                 "registros_microdato": 0, "poblacion_ponderada": 0})
                rec["dominios"] += 1
                rec["registros_microdato"] += d["conteos"]["registros_microdato"]
                rec["poblacion_ponderada"] += d["conteos"]["poblacion_ponderada"]
            return list(por_tamano.values())
        raise AssertionError(f"Pipeline desconocido: {pipeline}")


class InformeExploratorio(unittest.TestCase):
    def test_generacion_de_reporte_sin_mongodb(self):
        # El reporte no conecta con Mongo en esta prueba; se provee un doble
        # de importación únicamente cuando pymongo no está instalado.
        if importlib.util.find_spec("pymongo") is None:
            sys.modules["pymongo"] = types.SimpleNamespace(MongoClient=object)
        spec = importlib.util.spec_from_file_location("reporte_eic", ROOT / "07_analisis_perfiles.py")
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        docs = json.loads((ROOT / "salidas/indicadores_territoriales.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as dest:
            csv, informe, medias = modulo.ejecutar(ColeccionSimulada(docs), Path(dest), agrupacion=5)
            texto = informe.read_text(encoding="utf-8")
            self.assertTrue(csv.exists())
            self.assertTrue(medias.exists())
            self.assertIn("153", texto)
            self.assertIn("18.54 puntos porcentuales", texto)
            self.assertIn("media", texto.lower())
            self.assertIn("Conclusiones y recomendaciones", texto)
            self.assertIn("no es", texto.lower())


if __name__ == "__main__":
    unittest.main()
