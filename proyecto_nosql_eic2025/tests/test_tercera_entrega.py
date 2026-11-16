"""Pruebas sin Docker: sintaxis de agregaciones y no confusión entre 5 y 4 tamaños."""
import unittest
from analisis.consultas import (METRICAS, filtro_territorial, pipeline_dominios,
                               pipeline_conteos_por_tamano, pipeline_extremos,
                               pipeline_promedio_dominios_por_tamano)

class ConsultasMongoDB(unittest.TestCase):
    def test_filtrado_territorial(self):
        self.assertEqual(filtro_territorial(["01", "32"], ["1"]), {
            "territorio.cve_ent": {"$in": ["01", "32"]},
            "territorio.tamloc": {"$in": ["1"]},
        })

    def test_pipeline_usa_operaciones_de_rubrica(self):
        ops = [next(iter(x)) for x in pipeline_dominios(["01"], ["1"], 10)]
        self.assertEqual(ops, ["$match", "$project", "$sort", "$limit"])
        self.assertIn("$group", [next(iter(x)) for x in pipeline_conteos_por_tamano()])
        self.assertIn("$group", [next(iter(x)) for x in pipeline_extremos("escolaridad_promedio")])

    def test_solo_metricas_permitidas(self):
        with self.assertRaises(ValueError):
            pipeline_extremos("dato_no_autorizado")
        for nombre in METRICAS:
            self.assertTrue(pipeline_extremos(nombre))

    def test_agregacion_promedio_dominios(self):
        p = pipeline_promedio_dominios_por_tamano("escolaridad_promedio", ["01"], ["1", "2"])
        self.assertEqual([next(iter(stage)) for stage in p],
                         ["$match", "$match", "$group", "$sort"])
        self.assertEqual(p[0]["$match"]["territorio.cve_ent"], {"$in": ["01"]})
        self.assertEqual(p[2]["$group"]["media_no_ponderada_de_dominios"],
                         {"$avg": "$indicadores.escolaridad_promedio"})
        with self.assertRaises(ValueError):
            pipeline_promedio_dominios_por_tamano("dato_no_autorizado")

    def test_limite(self):
        with self.assertRaises(ValueError):
            pipeline_dominios(limite=20000)

if __name__ == "__main__":
    unittest.main()
