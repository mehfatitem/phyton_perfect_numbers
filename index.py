#!C:\Python36\python
import cgi
form = cgi.FieldStorage()
import signal

print("Content-Type: text/html")    # HTML is following
print()

title = "Anahtar Kelimeyi Giriniz..."

template = "<html>"
template += "<head></head>"
template += "<body>"
template += "<form align='center' id='form' name='form' action='index.py' method='post'>"
template += "<input type='text' id='input' name='input' placeholder='"+title+"' title='"+title+"'/></br></br>"
template += "<input type='submit' id='button' name='button' value='Hesapla'/>"
template += "</form>"
template += "</body>"
template += "</html>"

print(template)

def showMessage(msg , color = "red" , weight = "bold") :
	print("<p style='color:" + color + ";text-align:center;font-weight:" + weight + ";'>" + msg + "</p>")


title = form.getvalue("input").strip()
submit = form.getvalue("button").strip()

if title == "Mukemmel Sayilar" :
	total = 0
	counter = 0
	showMessage(title.upper() + "</br>")
	print("<table border='1' align='center'><thead><tr><th>Sıra</th><th>Sayı</th></tr></thead>")
	for i in range(2,10001) :
	 	tmp = int(i/2)
	 	tmp += 1
	 	for j in range(1,tmp) :
	 		if i % j == 0 :
	 			total += j
	 	if total == i :
	 		counter += 1
	 		msg = str(counter) + "."
	 		msg2 = str(i)
	 		print("<tr><td>"+msg+"</td><td><b style='color:red;'>"+msg2+"</b></td></tr>")
	 	total = 0
	print("</table>")
else :
	showMessage("Girmiş olduğunuz anahtar kelime yanlış!")
