from flask import Flask, render_template, redirect, url_for
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('data_xml'))


@app.route('/api')
def data_xml():

    xml_data = ET.parse('templates/API_SH.IMM.MEAS_DS2_en_xml_v2_5381695.xml')
    root = xml_data.getroot()
    panama_data = []
    for data in root.findall("data"):
        for record in data.findall("record"):
            for field in record.findall("field"):
                if field.get("key") == "PAN":
                    panama_data.append({
                        "Country_or_Area": record.find("field[@name='Country or Area']").text,
                        "Item": record.find("field[@name='Item']").text,
                        "Year": record.find("field[@name='Year']").text,
                        "Value": record.find("field[@name='Value']").text
                    })

    return render_template('data.html', data=panama_data)


if __name__ == '__main__':
    app.run(debug=True)