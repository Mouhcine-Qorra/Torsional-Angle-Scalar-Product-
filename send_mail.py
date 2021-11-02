import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def email_sender_func(receiver, einleitung, i):
    result = []
    # Create the root message and fill in the from, to, and subject headers
    print('\tGetting Parameters...')
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Ausbildung Fachrichtung Fachinformatiker für Anwendungsentwicklung / Bewerbung'
    msgRoot['From'] = 'qorra.mouhcin@gmail.com'
    msgRoot["To"] = receiver
    password = '@Taro987654'
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgalternative = MIMEMultipart('alternative')
    msgRoot.attach(msgalternative)

    plain = f"""\
        {einleitung},
        
        
    ich weiß, dass Sie viele Bewerbungen haben und Sie können sie nicht alle berücksichtigen und auch akzeptieren. Es wäre sehr nett von Ihnen, wenn Sie meine Bewerbungsunterlagen lesen könnten.
Meine Erfahrung und Qualifikation stimmen eng mit den in der Ausschreibung genannten Aufgabenbereichen überein.
        
Ich habe versucht, mich von anderen bewerbern abzuheben, indem ich eine Website erstellt habe, die sowohl eine Portfolio als auch eine E-Commerce-Website enthält.

Das Projekt (Frontend und Backend) habe ich selbst gebaut. Ich hoffe, Sie wissen die Eingereichter Zeit und Mühe zu schätzen

Im anhang finden Sie die gewünschten unterlagen als PDF-Datei, und wenn ich Sie überzeugen könnte, freue ich mich sehr auf ein Vorstellungsgespräch.

    * Schauen Sie sich doch mein bisheriges Portfolio an. Hier der Link dazu: https://portfolio-mouhcin-qorra.herokuapp.com        
        
    * Hier ist der Link zu meiner E-Commerce-Site: https://portfolio-mouhcin-qorra.herokuapp.com/store

Einige Funktionen, die behandelt wurden:

    - Responsive Webdesign, verschiedene tolle Designs für jedes Gerät (Handys, Laptops und Tablets).
    - Benutzern nicht erlauben, zur Anmeldeseite zu gehen, wenn sie bereits angemeldet sind.
    - Wenn Sie Produkte in Ihren Warenkorb legen, bleiben diese auch dann erhalten, wenn Sie den Cache und die Cookies löschen.
    - Passwort zurücksetzen system (Sie können sich registrieren und abmelden, dann gehen und das Passwort zurücksetzen).
    - Auf jeder Produktdetailseite verändert das Erscheinungsbild der produkte im empfohlenen Abschnitt auf der Produktdetailseite.
      PS: Sie können Artikel in den Warenkorb legen und den Checkout-Prozess testen ohne Eingabe von Kreditkarteninformationen; Ich habe die Zahlungsintegration auf der Checkout-Seite deaktiviert.
    
Es wäre schön, wenn ich etwas von Ihnen hören würde.
    
    
Mit freundlichen Grüßen
Mouhcin Qorra


    """
    msgtext = MIMEText(plain, 'plain')
    msgalternative.attach(msgtext)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    html = f"""\
    <p style="margin-left: 1rem">{einleitung},<br><br><br></p>
    
    <p style="margin-left: .5rem">ich weiß, dass Sie viele Bewerbungen haben und Sie können sie nicht alle berücksichtigen und auch akzeptieren. Es wäre sehr nett von Ihnen, wenn Sie meine Bewerbungsunterlagen lesen könnten.</p><br>
    
    Meine Erfahrung und Qualifikation stimmen eng mit den in der Ausschreibung genannten Aufgabenbereichen überein.<br><br>
    
    Ich habe mich gefragt, wie ich auf einzigartige Weise bewerben kann, und kam dann auf die ldee, eine Website, die sowohl eine Portfolio als auch eine E-Commerce-Website enthält zu erstellen, in Anbetracht dessen, dass ich Webentwickler bin.<br><br>
    
    Ich habe lange Tag und Nacht gearbeitet, um das Projekt abzuschließen, weil ich es (Frontend und Backend) selbst gebaut habe.<br>
        
    Ich hoffe, Sie wissen die Eingereichter Zeit und Mühe zu schätzen<br><br>
    
    Im anhang finden sie die gewünschten unterlagen als PDF-Datei, und wenn ich Sie überzeugen könnte, freue ich mich sehr auf ein Vorstellungsgespräch.<br><br>
    
    <p style="margin-left: .5rem">* Schauen Sie sich doch mein bisheriges Portfolio an. Hier der Link dazu: <a href="https://portfolio-mouhcin-qorra.herokuapp.com"> https://portfolio-mouhcin-qorra.herokuapp.com</a></p><br>
    
    <p style="margin-left: .5rem">* Hier ist der Link zu meiner E-Commerce-Site: <a href="https://portfolio-mouhcin-qorra.herokuapp.com/store"> https://portfolio-mouhcin-qorra.herokuapp.com/store</a></p><br>
    
    <a href="https://portfolio-mouhcin-qorra.herokuapp.com/store"><img src="cid:Capture1" alt="Portfolio"></a><br><br>
    
    Einige Funktionen, die behandelt wurden:<br><br>
    
    <p style="margin-left: .5rem">- Responsive Webdesign, verschiedene tolle Designs für jedes Gerät (Handys, Laptops und Tablets).</p><br>
    <p style="margin-left: .5rem">- Benutzern nicht erlauben, zur Anmeldeseite zu gehen, wenn sie bereits angemeldet sind.</p><br>
    <p style="margin-left: .5rem">- Wenn Sie Produkte in Ihren Warenkorb legen, bleiben diese auch dann erhalten, wenn Sie den Cache und die Cookies löschen.</p><br>
    <p style="margin-left: .5rem">- Passwort zurücksetzen system (Sie können sich registrieren und abmelden, dann gehen und das Passwort zurücksetzen).</p><br>
    <p style="margin-left: .5rem">- Auf jeder Produktdetailseite verändert das Erscheinungsbild der produkte im empfohlenen Abschnitt auf der Produktdetailseite.</p><br>
    <p style="margin-left: .6rem">PS: Sie können Artikel in den Warenkorb legen und den Checkout-Prozess testen; Ich habe die Zahlungsintegration auf der Checkout-Seite deaktiviert.</p><br><br>
    
    Es wäre schön, wenn ich etwas von Ihnen hören würde.<br><br><br>
    
    Mit freundlichen Grüßen<br>
    
    Mouhcin Qorra<br><br>
    """
    msgtext = MIMEText(html, 'html')
    msgalternative.attach(msgtext)

    print('\tGetting PDF & Image...')
    # This example assumes the image is in the current directory
    fp = open('SCREEN.png', 'rb')
    msgimage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgimage.add_header('Content-ID', '<Capture1>')
    msgimage.add_header('Content-Disposition', 'inline', filename='Portfolio')
    msgRoot.attach(msgimage)

    # Pdf attach
    binary_pdf = open('MouhcinPDF.pdf', 'rb')
    payload = MIMEBase('application', 'octate-stream', Name='Lebenslauf-Mouhcin-Qorra.pdf')
    payload.set_payload(binary_pdf.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename='Lebenslauf-Mouhcin-Qorra.pdf')
    msgRoot.attach(payload)

    print('\tConnecting to gmail...')
    server = smtplib.SMTP('smtp.gmail.com:587')
    try:
        server.ehlo()
        server.starttls()
        server.ehlo()
        print('\tlogin to your account...')
        server.login('qorra.mouhcin@gmail.com', password)
        print('\tSending email...')
        server.sendmail('qorra.mouhcin@gmail.com', receiver, msgRoot.as_string())
        print(f'\tEmail sent successfully to:\t\t\t {receiver}')
    except Exception as e:
        result.append(f'did not send to {receiver} in line: {i} because of {e}')
    finally:
        server.quit()
        print('Quit...')
    if result:
        return result
