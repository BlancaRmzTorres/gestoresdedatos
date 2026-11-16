"""Pruebas en CSV sintetico. No usan datos oficiales ni requieren Docker."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PruebasPipeline(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for archivo in ('config.py', 'ejecutar_pipeline.py', '01_diagnostico.py',
                        '02_preparar_microdatos.py', '03_construir_indicadores.py',
                        '04_generar_documentos_json.py', 'verificar_documentos.py'):
            (self.root / archivo).write_bytes((ROOT / archivo).read_bytes())
        (self.root / 'src').mkdir()
        (self.root / 'src' / '__init__.py').write_bytes((ROOT / 'src' / '__init__.py').read_bytes())
        (self.root / 'src' / 'transformaciones.py').write_bytes((ROOT / 'src' / 'transformaciones.py').read_bytes())
        (self.root / 'datos').mkdir()
        from config import VARIABLES  # from test suite original root if invoked from root
        plantilla = dict.fromkeys(VARIABLES, '')
        def fila(i, ent, tam, sexo, edad, factor, conact, hnv):
            d = dict(plantilla)
            d.update(ID_PERSONA=f'ID{i:04d}', ID_VIV='VIV01', CVE_ENT=ent, CVE_MUN='001',
                     TAMLOC=tam, FACTOR=factor, SEXO=sexo, EDAD=edad, NIVACAD='09',
                     ESCOACUM='12', CONACT=conact, SITUA_CONYUGAL='01',
                     PERTE_INDIGENA='3', HLENGUA='3', HIJOS_NAC_VIVOS=hnv,
                     FECHA_NAC_M='01', FECHA_NAC_A='2024')
            return d
        rows = [fila(1,'01','1','3','30','2','10','2'),
                fila(2,'01','1','3','35','3','50','1'),
                fila(3,'01','5','3','20','4','10','0'),
                fila(4,'02','1','3','35','5','10','2'),
                fila(5,'01','1','1','30','8','10','3'), # excluir hombre
                fila(6,'01','1','3','60','8','10','3'), # excluir 60+ años
                fila(7,'01','4','3','20','6','50','3')] # combinar con categoría 5
        self.csv = self.root / 'datos' / 'personas00.csv'
        with self.csv.open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=VARIABLES);w.writeheader();w.writerows(rows)

    def test_pipeline_completo_sintetico(self):
        r = subprocess.run([sys.executable, str(self.root/'ejecutar_pipeline.py'),
                            '--archivo','datos/personas00.csv','--chunksize','2'],
                           cwd=self.root, capture_output=True,text=True)
        self.assertEqual(r.returncode,0,msg=r.stdout+'\n'+r.stderr)
        docs=json.loads((self.root/'salidas'/'indicadores_territoriales.json').read_text(encoding='utf-8'))
        self.assertEqual(len(docs),4)
        self.assertEqual({d['_id'] for d in docs},{'01_1','01_4','01_5','02_1'})
        doc=next(x for x in docs if x['_id']=='01_1')
        self.assertEqual(doc['conteos']['registros_microdato'],2)
        self.assertEqual(doc['conteos']['poblacion_ponderada'],5)
        self.assertAlmostEqual(doc['indicadores']['participacion_economica_pct'],40,places=4)
        # El nuevo producto de 4 tamaños mantiene 1/2/3 y agrupa 4+5;
        # no crea un pseudoindicador con promedios de promedios.
        docs4=json.loads((self.root/'salidas'/'indicadores_territoriales_4.json').read_text(encoding='utf-8'))
        self.assertEqual({d['_id'] for d in docs4}, {'01_1','01_4','02_1'})
        d4=next(d for d in docs4 if d['_id']=='01_4')
        self.assertEqual(d4['conteos']['poblacion_ponderada'], 10)
        self.assertAlmostEqual(d4['indicadores']['promedio_hijos_nacidos_vivos'], 1.8, places=6)
        self.assertIn('hnv_den', d4['componentes'])
        r2 = subprocess.run([sys.executable, str(self.root/'verificar_documentos.py')],
                            cwd=self.root,capture_output=True,text=True)
        self.assertEqual(r2.returncode,0,msg=r2.stderr)

    def test_duplicados_entre_bloques_sqlite(self):
        with self.csv.open('r', encoding='utf-8', newline='') as f:
            rows=list(csv.DictReader(f))
        rows[-1]['ID_PERSONA'] = rows[0]['ID_PERSONA']
        with self.csv.open('w', encoding='utf-8', newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
        r = subprocess.run([sys.executable, str(self.root/'01_diagnostico.py'),
                            '--archivo', str(self.csv), '--chunksize', '2',
                            '--modo-duplicados', 'disco'],
                           cwd=self.root, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, msg=r.stderr)
        self.assertIn('Duplicados por ID_PERSONA: 1',r.stdout)

    def test_ruta_csv_inexistente(self):
        r = subprocess.run([sys.executable,str(self.root/'ejecutar_pipeline.py'),
                            '--archivo','datos/noexiste.csv'],cwd=self.root,
                           capture_output=True,text=True)
        self.assertNotEqual(r.returncode,0)
        self.assertIn('No existe el CSV',r.stderr)

if __name__=='__main__':
    unittest.main()
