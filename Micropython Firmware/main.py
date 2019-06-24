
def web_page():
  if motor.value() == 1:
    button_render ='<p><a href="/?pump=stop"><button class="button button2">STOP</button></a></p>'
  #elif valveB.value() == 1:
  #""" + button_render + """
  else:
    button_render = '<p><a href="/?pump=on"><button class="button">INFLATE</button></a></p><p><a href="/?pump=off"><button class="button button2">DEFLATE</button></a></p>'
  
  html = """<html><head> <title>Infatable Cushion</title> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}.button2{background-color: #4286f4;}</style></head><body> <h1>Infatable Cushion</h1> """ + button_render + """</body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  inflate = request.find('/?pump=on')
  deflate = request.find('/?pump=off')
  stop = request.find('/?pump=stop')
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
  if inflate == 6:
    print('INFLATE')
    led.value(0)
    motor.value(0)
    valveA.value(0)
    valveB.value(1)

  if deflate == 6:
    print('DEFLATE')
    led.value(0)
    motor.value(0)
    valveA.value(1)
    valveB.value(0)

  if stop == 6:
    print('STOP')
    led.value(1)
    motor.value(1)
    valveA.value(1)
    valveB.value(1)