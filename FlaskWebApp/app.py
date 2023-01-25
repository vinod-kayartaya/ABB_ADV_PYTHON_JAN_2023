from flask import Flask, jsonify, make_response, request
import uuid


app = Flask('Contacts REST service')
contacts = [
    {
        "id": "582841db-7cbf-42fb-aade-6f001e575cf2",
        "firstname": "Tamiko",
        "lastname": "Teager",
        "gender": "Female",
        "email": "tteager0@admin.ch",
        "phone": "352-522-8049",
        "city": "Poitiers"
    }, {
        "id": "3a1c5c55-c5e3-488d-b1ec-d247b59cbbc4",
        "firstname": "Howard",
        "lastname": "Ghelardoni",
        "gender": "Male",
        "email": "hghelardoni1@taobao.com",
        "phone": "863-729-8045",
        "city": "Öndörhoshuu"
    }, {
        "id": "c06ab6bc-c646-463d-8b7f-44840bd22424",
        "firstname": "Sherwynd",
        "lastname": "Itzhaiek",
        "gender": "Male",
        "email": "sitzhaiek2@miitbeian.gov.cn",
        "phone": "870-296-3255",
        "city": "Złotniki Kujawskie"
    }, {
        "id": "d801f5e8-bec2-4558-ba5b-6fa5bac7d93d",
        "firstname": "Marcos",
        "lastname": "Petroselli",
        "gender": "Male",
        "email": "mpetroselli3@alibaba.com",
        "phone": "256-837-9032",
        "city": "Niort"
    }, {
        "id": "acf4b792-67f0-421d-8865-7dd44df3b65e",
        "firstname": "Claiborne",
        "lastname": "Ansill",
        "gender": "Male",
        "email": "cansill4@columbia.edu",
        "phone": "249-315-8248",
        "city": "Hamburg"
    }, {
        "id": "92850eb5-0eb3-4087-b2ab-e527917093dd",
        "firstname": "Patrice",
        "lastname": "Seale",
        "gender": "Male",
        "email": "pseale5@com.com",
        "phone": "996-303-5314",
        "city": "Kagoshima-shi"
    }, {
        "id": "c649c54d-64c4-472d-8b41-a02f2946140c",
        "firstname": "Les",
        "lastname": "Leverette",
        "gender": "Male",
        "email": "lleverette6@soundcloud.com",
        "phone": "427-209-1769",
        "city": "Chernukha"
    }, {
        "id": "beb1706b-363c-4e75-b902-332d0ee5cdeb",
        "firstname": "Raymund",
        "lastname": "Ordish",
        "gender": "Male",
        "email": "rordish7@mac.com",
        "phone": "250-905-8402",
        "city": "Yokkaichi"
    }, {
        "id": "3f5b3f59-966d-41ba-9c67-8a8f4a046d54",
        "firstname": "Lori",
        "lastname": "Lavies",
        "gender": "Female",
        "email": "llavies8@whitehouse.gov",
        "phone": "221-290-6617",
        "city": "Trà Vinh"
    }, {
        "id": "4d8a089d-c796-4a2f-a86e-6ed76d4b1da7",
        "firstname": "Athene",
        "lastname": "Diglin",
        "gender": "Female",
        "email": "adiglin9@flickr.com",
        "phone": "334-480-3840",
        "city": "Komsomolets"
    }, {
        "id": "a79ae525-f617-40b3-8116-e81decd2d8d8",
        "firstname": "Brandyn",
        "lastname": "Galvan",
        "gender": "Male",
        "email": "bgalvana@pinterest.com",
        "phone": "370-197-0210",
        "city": "Huating"
    }, {
        "id": "fd0e5ac2-b036-407d-b219-eabb34da0272",
        "firstname": "Chanda",
        "lastname": "McQuirk",
        "gender": "Female",
        "email": "cmcquirkb@unesco.org",
        "phone": "878-732-4811",
        "city": "Bauang"
    }, {
        "id": "19cdc5b4-74df-42ec-bf7d-e18d95ee4e6e",
        "firstname": "Laird",
        "lastname": "Winsor",
        "gender": "Male",
        "email": "lwinsorc@seesaa.net",
        "phone": "819-610-8779",
        "city": "Kremenets’"
    }, {
        "id": "f7146800-53ea-47e1-88d5-d03f8a1e51c4",
        "firstname": "Elliott",
        "lastname": "Meeron",
        "gender": "Male",
        "email": "emeerond@elegantthemes.com",
        "phone": "497-315-4127",
        "city": "Gaojian"
    }, {
        "id": "8dfdb2fc-4395-4843-b674-42ff07b857ca",
        "firstname": "Easter",
        "lastname": "McNair",
        "gender": "Female",
        "email": "emcnaire@stanford.edu",
        "phone": "867-929-5155",
        "city": "Arzila"
    }, {
        "id": "be0958c9-30af-499a-adcb-5e675b11190b",
        "firstname": "Evaleen",
        "lastname": "Hadye",
        "gender": "Female",
        "email": "ehadyef@jalbum.net",
        "phone": "706-747-0589",
        "city": "Sukonolo Krajan"
    }, {
        "id": "474f8ac4-2554-4718-a627-2db618e6790a",
        "firstname": "Hastie",
        "lastname": "Lisamore",
        "gender": "Male",
        "email": "hlisamoreg@businessweek.com",
        "phone": "765-727-3132",
        "city": "Bailieborough"
    }, {
        "id": "82d1944d-993e-47b5-b775-1c172f51b3ee",
        "firstname": "Horton",
        "lastname": "Witton",
        "gender": "Male",
        "email": "hwittonh@mozilla.org",
        "phone": "927-335-1460",
        "city": "Jiantianjie"
    }, {
        "id": "b430e3ab-ca43-46bb-a9ca-7e1ad0faf9fd",
        "firstname": "Randolf",
        "lastname": "Wilce",
        "gender": "Male",
        "email": "rwilcei@ted.com",
        "phone": "664-408-0754",
        "city": "San José Poaquil"
    }, {
        "id": "a329f18d-80d8-4353-ac87-0cb0a40d9191",
        "firstname": "Lavena",
        "lastname": "Babington",
        "gender": "Female",
        "email": "lbabingtonj@deliciousdays.com",
        "phone": "214-328-0685",
        "city": "Tras Cerros"
    }, {
        "id": "58405c7e-c6a1-4297-9f72-c365e660a8be",
        "firstname": "Christie",
        "lastname": "Claffey",
        "gender": "Female",
        "email": "cclaffeyk@oaic.gov.au",
        "phone": "169-801-6909",
        "city": "Kawungsari"
    }, {
        "id": "3c7e34d6-1012-492f-aed6-2a17ca6dd32f",
        "firstname": "Nathanil",
        "lastname": "Annandale",
        "gender": "Male",
        "email": "nannandalel@phoca.cz",
        "phone": "446-135-8020",
        "city": "Madang"
    }, {
        "id": "13640fff-0f3b-409f-bd0c-9e2fd59378e4",
        "firstname": "Giorgio",
        "lastname": "Willstrop",
        "gender": "Male",
        "email": "gwillstropm@google.com.hk",
        "phone": "265-376-8828",
        "city": "Ambatofinandrahana"
    }, {
        "id": "05050247-cc05-41cd-a3eb-badf4253e65a",
        "firstname": "Bree",
        "lastname": "Mergue",
        "gender": "Female",
        "email": "bmerguen@cisco.com",
        "phone": "403-166-6966",
        "city": "Uście Gorlickie"
    }, {
        "id": "d6e1563b-1d0c-4bd4-a71b-d25a6931907c",
        "firstname": "Galven",
        "lastname": "McCloid",
        "gender": "Male",
        "email": "gmccloido@berkeley.edu",
        "phone": "339-304-9851",
        "city": "Itajaí"
    }, {
        "id": "92f31e48-df6a-418a-819d-310e9756cdc4",
        "firstname": "Rafa",
        "lastname": "De Brett",
        "gender": "Female",
        "email": "rdebrettp@sfgate.com",
        "phone": "207-234-8126",
        "city": "San Vicente Pacaya"
    }, {
        "id": "047022d0-d784-41b7-b72f-752be92011ed",
        "firstname": "Addie",
        "lastname": "McDonell",
        "gender": "Male",
        "email": "amcdonellq@blogtalkradio.com",
        "phone": "103-448-5277",
        "city": "Saskylakh"
    }, {
        "id": "306371ba-e11c-47af-a437-a515cd7dfa8f",
        "firstname": "Ellsworth",
        "lastname": "Daft",
        "gender": "Male",
        "email": "edaftr@disqus.com",
        "phone": "886-539-2857",
        "city": "Châteauroux"
    }, {
        "id": "14335df4-5fd3-4991-9119-b28732d6eba6",
        "firstname": "Nikolia",
        "lastname": "Madrell",
        "gender": "Female",
        "email": "nmadrells@xrea.com",
        "phone": "818-886-1029",
        "city": "Andamui"
    }, {
        "id": "84224152-1e19-46c0-885c-8ed1dc6160f9",
        "firstname": "Wolfy",
        "lastname": "Bainbridge",
        "gender": "Male",
        "email": "wbainbridget@bloomberg.com",
        "phone": "556-560-4569",
        "city": "Mengmeng"
    }, {
        "id": "0ad413f4-41d5-404a-88d5-8570ddfb344d",
        "firstname": "Nataline",
        "lastname": "Pilgrim",
        "gender": "Female",
        "email": "npilgrimu@plala.or.jp",
        "phone": "444-339-8061",
        "city": "Alor Star"
    }, {
        "id": "aea6d3ac-f3e4-4fdb-be49-da9e934b0920",
        "firstname": "Marc",
        "lastname": "Maiden",
        "gender": "Male",
        "email": "mmaidenv@ow.ly",
        "phone": "499-951-9703",
        "city": "La Laguna"
    }, {
        "id": "0e778ea7-cbba-424b-9952-7e94957288ce",
        "firstname": "Early",
        "lastname": "Arlt",
        "gender": "Male",
        "email": "earltw@lycos.com",
        "phone": "115-501-0675",
        "city": "Yefremov"
    }, {
        "id": "d05ddadd-1fd5-46e8-884c-1cd9e3014e98",
        "firstname": "Fulton",
        "lastname": "Scripture",
        "gender": "Male",
        "email": "fscripturex@weather.com",
        "phone": "411-578-3976",
        "city": "Mishkino"
    }, {
        "id": "19330945-90fb-40d3-a87f-610fe9328c0a",
        "firstname": "Flint",
        "lastname": "Tschierse",
        "gender": "Male",
        "email": "ftschiersey@constantcontact.com",
        "phone": "774-270-7905",
        "city": "Carania"
    }, {
        "id": "f1dc6458-bb31-4b0f-b957-6ca580884706",
        "firstname": "Tamqrah",
        "lastname": "Moller",
        "gender": "Female",
        "email": "tmollerz@sciencedaily.com",
        "phone": "273-741-3522",
        "city": "Botevgrad"
    }, {
        "id": "5c42e5a0-1c47-4ee6-9dee-4e698b06e2f5",
        "firstname": "Ailbert",
        "lastname": "Rosewell",
        "gender": "Male",
        "email": "arosewell10@who.int",
        "phone": "178-849-4365",
        "city": "Ḩarf al Musaytirah"
    }, {
        "id": "1c6131cd-c909-4119-ad2b-b5c3dc1202b2",
        "firstname": "Fredericka",
        "lastname": "Walczynski",
        "gender": "Female",
        "email": "fwalczynski11@infoseek.co.jp",
        "phone": "605-644-8960",
        "city": "Líbano"
    }, {
        "id": "06df18f3-a646-429b-bd40-6829999c5fb2",
        "firstname": "Vinnie",
        "lastname": "Puddephatt",
        "gender": "Male",
        "email": "vpuddephatt12@prlog.org",
        "phone": "134-482-5043",
        "city": "Weixin"
    }, {
        "id": "2155c1bc-e145-47eb-98b7-b8b70cf6dd7f",
        "firstname": "Haven",
        "lastname": "Lavell",
        "gender": "Male",
        "email": "hlavell13@odnoklassniki.ru",
        "phone": "539-752-7692",
        "city": "Zhenjiang"
    }, {
        "id": "cf2f0b9c-74a9-451b-8096-2d04171a1dbc",
        "firstname": "Lindon",
        "lastname": "Gruszczak",
        "gender": "Male",
        "email": "lgruszczak14@businessweek.com",
        "phone": "808-866-0808",
        "city": "Baicheng"
    }, {
        "id": "beaecbe3-5fe7-4220-83a7-436334c15c44",
        "firstname": "Blancha",
        "lastname": "Ableson",
        "gender": "Female",
        "email": "bableson15@admin.ch",
        "phone": "484-345-9562",
        "city": "Ozerki"
    }, {
        "id": "7380f124-45e8-4923-a1a6-da3de6a2ee26",
        "firstname": "Joyan",
        "lastname": "Davitashvili",
        "gender": "Female",
        "email": "jdavitashvili16@blogger.com",
        "phone": "802-440-2903",
        "city": "Naranjito"
    }, {
        "id": "7c90e86e-a493-41d1-8d55-5b47de216fd8",
        "firstname": "Brana",
        "lastname": "Mates",
        "gender": "Female",
        "email": "bmates17@wired.com",
        "phone": "564-471-2753",
        "city": "Buenos Aires"
    }, {
        "id": "ee9f2d7e-2c84-43bf-a70f-0d1503999cdc",
        "firstname": "Christoffer",
        "lastname": "Snap",
        "gender": "Male",
        "email": "csnap18@harvard.edu",
        "phone": "522-391-1117",
        "city": "Nanfeng"
    }, {
        "id": "99fe6d23-53ad-4407-af37-3289487162be",
        "firstname": "Stephi",
        "lastname": "Kinlock",
        "gender": "Female",
        "email": "skinlock19@shinystat.com",
        "phone": "807-454-4990",
        "city": "Fažana"
    }, {
        "id": "de5eeb10-42be-4115-b9ba-c0e3d0e199c1",
        "firstname": "Daphna",
        "lastname": "Tourne",
        "gender": "Female",
        "email": "dtourne1a@sitemeter.com",
        "phone": "339-291-4422",
        "city": "Ojos de Agua"
    }, {
        "id": "436b94c6-5578-4f19-9f03-74ffbc59000b",
        "firstname": "Louis",
        "lastname": "Eusden",
        "gender": "Male",
        "email": "leusden1b@dot.gov",
        "phone": "409-237-0575",
        "city": "Manhumirim"
    }, {
        "id": "18b0c6ad-6712-4e47-bdb2-a56816133d2e",
        "firstname": "Simona",
        "lastname": "Crone",
        "gender": "Female",
        "email": "scrone1c@diigo.com",
        "phone": "738-556-6220",
        "city": "Ursynów"
    }, {
        "id": "97439c88-e018-41d6-ac18-02586917546b",
        "firstname": "Berthe",
        "lastname": "Wyre",
        "gender": "Female",
        "email": "bwyre1d@networkadvertising.org",
        "phone": "456-503-7597",
        "city": "Guiset East"
    }]


@app.get('/api/contacts')
def get_contacts():
    accept = request.headers.get('Accept')

    if accept == 'text/plain':
        resp = make_response('This will produce list of contacts, if request mimetype is application/json')
        resp.mimetype = accept
    elif accept == 'application/json':
        resp = make_response(contacts)
        resp.mimetype = accept
    else:
        resp = make_response('Request data format is not available', 406)
        resp.mimetype = 'text/plain'

    return resp


@app.get('/api/contacts/<string:contact_id>')
def get_one_contact(contact_id):
    data = [c for c in contacts if c['id'] == contact_id]
    if len(data) == 0:
        err = dict(message='No data found for given id')
        return make_response(err, 404)
    else:
        return jsonify(data[0])


@app.post('/api/contacts')
def add_new_contact():
    new_contact = request.json
    new_contact['id'] = str(uuid.uuid4())

    # check for the presence of firstname, email, phone
    if 'firstname' not in new_contact or 'email' not in new_contact or 'phone' not in new_contact:
        err = dict(message='firstname, email and phone are mandatory. one or more of them are missing')
        return make_response(err, 400)

    global contacts
    # check for phone
    data = [c for c in contacts if c['phone'] == new_contact['phone']]
    if len(data) > 0:
        err = dict(message=f'Contact with this phone ({new_contact["phone"]}) already exists')
        return make_response(err, 400)

    # check for email
    data = [c for c in contacts if c['email'] == new_contact['email']]
    if len(data) > 0:
        err = dict(message=f'Contact with this email ({new_contact["email"]}) already exists')
        return make_response(err, 400)

    contacts.append(new_contact)
    return make_response(new_contact, 201)


if __name__ == '__main__':
    app.run(port=2345, host='0.0.0.0', debug=True)
