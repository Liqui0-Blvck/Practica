import cx_Oracle

querys = []
data = []
try:
  conn = cx_Oracle.connect(user='test', password='1234', dsn='localhost/xepdb1', encoding='utf8')
  print('conexion exitosa')


  cur = conn.cursor()

  query = """ SELECT tr.total,
              pr.nombre FROM transaccion tr JOIN item it 
              on tr.id_transaccion = it.transaccion_id 
              JOIN evento ev on it.evento_id = ev.id_evento 
              JOIN actividad ac on ev.actividad_id = ac.id_actividad 
              JOIN proveedor pr on ac.proveedor_id = pr.id_proveedor 
              WHERE ac.id_actividad in (1,2,3) 
              ORDER BY tr.total desc """
  
  if querys == []:
    each_query = []
    each_query.append(query)
    querys.append(each_query)
  else:
    print(querys)

  for i in range(len(querys)):
    cur.execute(querys[i][0])
    rows = cur.fetchall()
  for row in rows:
    data.append(row)
  print(data)

except:
  print('no pudiste conectarte')

