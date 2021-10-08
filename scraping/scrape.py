import requests, json
from bs4 import BeautifulSoup

# run
# a = [...document.querySelectorAll("#tblResults tr a")].map(e => e.href)
# in devtools console of the results of a search to get URLs
urls = ["http://www.matweb.com/search/DataSheet.aspx?MatGUID=4e6a4852b14c4b12998acf2f8316c07c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9fd0a41bf0eb40c4ae7d73d5dec1c1d6",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=503232647ec44a408f191d57dd336ea5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=15c8581a40f54c5494ab998ffc569971",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=5e4ae9a0cf7f40d1b15326f36cadb6e5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0ca942a869a14901b54606e3007d1c25",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=15c89e1b04bb4f7e976b7ed003c8a257",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e994edba533c4cdaa512e455b5ee400f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=987d2403a49841a7b59ae89ab11fb1c7",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=3091e2deec9c450aa3b903cc028ce5cd",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=a39cbb3aee8944259f0146ec21cbbfcf",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0b8bc019ee4b4d8ba35e7835b1e803c2",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9d88870cabe84aad823bcfed0b9ce00f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=345552bb38074138b63c8c3d936a7329",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f311ea86cd814ff8b7a70efb42eb9f41",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=891752cabcb4448db3a84e0814c15d2c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b910504d247f418e8e70a10ad0f549c2",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=01e54466915345a1b17f2dfbfe8daf24",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4b809e646f4b4388ad11d46e8f371db7",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8086715ebd994c8db7f81b0a784f2069",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e7fd7da733c8410ea31694f1636c7bb5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8fa984ef30804ff9acb13f884c42d12d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=5bc55013c5b14ccfa05920e2b91be656",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b9ff95a9353144559007d9fc71c20dd0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=5a005487e02e4e18b894b7867c3772f4",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=6099b550e8bb4d2baea27046a8af9e34",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4f409bf3b3df4dc2a0d2176b33eb0876",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=ac0c011a4d6a4948ac7b56c07f91b95f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d1e286e1ac0742358544b953bbf3c2e9",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=23d7f35662424675aad7df2e984109f6",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=23a456922c4d4bb4b15519ed1c50c47f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=a812783cd8d44cfc89a8ccd8801d6968",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=efb1f4e2d54f4fee97253566ae77a478",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e81653f006ba4e2b916d2a7ca4a4b101",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=2f831d3ba75c450590bd3146575cf16f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=412c4207b81f416c8331dd8af44bbdb9",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=435d1094ebac4149ac62648daba849a5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9cd99c9e8dea4d29a71158b837e98b89",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=63d3406647a04540b3b2e2efedcf0601",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=3f583bbc40d44c40bd55bdae7b122160",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4a00b2d85a4541dd855412e299d7a611",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d591ab3bc07a49039582efb8de674acd",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f459463aa21d4a6c83123cf0b3d91b0e",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=fdf4fc3706f14c8784ddc282dc505632",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=be17820e155a4fd4a30cbd28edd14f10",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0e889fa9668d45f2b015bf2f43f6b61b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=007b91ae31ba4930b218924682bd2e1d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=ea14a88a576a45f08ff009fb5749df15",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8c8cad8fe20544508f41b4a1300af4a1",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0ada036e31fb444eaa84e411021e2214",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=167aa28849f7445c88ba2300a4ba5c88",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=15ee784a488e4ba790fa0e93c3a65972",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8f0eab8295a947ee9addf50d2e1c896c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b055d0346b6d4f438000ed77829fe4ce",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=6a9fb156317c4ca8ab00bf8443eb13b3",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9860f0fd41534f6bbe53a7ae968c705a",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=07baafbb9c364fb18fd413bceced867f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=2ab3ecbb63da45e0924b67dae6095472",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=7855682f98ce4e038f9148ad464a99c0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c2809f73004141b6b139d21b12341f69",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=091ad52e001b4f4a9e65eb7c274d5947",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=62beac394de6495eaff845ab62e237ff",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=7c7eaebc82b942bb85ea8022bace03cf",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=618f942218dc48d6a1830105ad562b96",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d730b7bbd11249fcb79c0106fb8c31a9",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f561c75d983f4b6592e71cb5f8d3f430",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4ac3557f498747aaa6ad0ffbeb405a7d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=55e7fc8aba61433f9088f5a059b2eac2",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=33b338d959e4420da22c6772476e9608",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=251d988ad2f14fbb907ee498d6c61db4",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=eb827a6ba240453fa33d1c662269b56b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d21cedd3ba5a4c219080cd3d587edb22",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=ff9e89cd1ab444c898a57de877f33d3d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=fbadd86efaa548e7a315448462af0fb9",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=7142e63b11c541d6b07b4eb563d04159",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b892791043a248ee940093b430b13d78",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=ba535f3597b04d65a30fbcaef202a194",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d69b9ce368ff41319d8478b7a975f6c5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=043336de670d44a9b514976dd8130c67",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9aef2300ed7542d28fdc9ad70f4bbebb",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=066a52c1864f4b33b04a58677747b3f3",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f5758a93b5bb447282641e90a824e82b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b8ad06d512a84751b567481706bccb60",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0db28f8dee0c45c0886b0b9e11ec283a",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c2e825e5fde14a9f8e5afbb0c444a531",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=3b682321dcc3467f99b442b9aa345501",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=dc69c8426f1e44398485ffe54d47fb92",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4b8a8c13cf354fc5893a40cf8eca022c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0fcb26f165df49899334d509d8e972f9",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f41ac8bc1ddd4c1d85247e646b3ec2be",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=13b06572615944eb933ac7a95c6b636b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=bab6f5a145384499a9fe6816dd74cb32",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=57992fdd32f1481db247b3b1b4d0c8b8",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=60c6563074c14686b1c9f2fdb43a614d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4876b83a410a4f9f97f232514e016a1b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4d238954f08d44fc8a1aa90597f9d57b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c0d517ecb6f040c7b9f2136c94aa6af8",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=0d2a4c5a403c4d728b1af19ba7b818e0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=889c8227b45e46399b08a4185e2dc345",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=7c08b6e11b83498595994285ea75d486",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=eceac563faf747b6b7cb1391c30d109d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f878e7f98b5b48b899cacd25981628ff",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=eae04ccd9702434b9b2b4b5dd4969a86",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=3fd3756c6d42449ea2a7a9497a62f07f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=32d3c03bce52440194505ed6a170956e",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=141554316fac48448a2ce7550b20851e",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=cf4250b3eb254afe8a13febbbf14431d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=2b98d1c524174ef1a7aec46a8bed7f62",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=458840d7b46f43f0b96647d2ed0ce211",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=1d599876cfcf468a95ea0fded85aa503",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=a9f88e2c14a44aafb98861c88270323a",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=4886b8f83d3f4e14882beacd503cd174",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=90d2472a4c0442e88ff51f4a48ec605e",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=cc0bc07c64854f11aa16ead340d615bc",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=295aabe916174d048c9571c27c455fee",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=44e2b95633cb4e37b57715500d01d52c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e832b474185d469f91de6de81538527c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=6ad6bcf723834f2dbc57deb0f6f5a901",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=72b84a455e7f437092c8067db942142b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=74d393fc725f4d48abce52b9a7099b48",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=57fac0c95c5c44268a012e9ff1d66085",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=797de3c3cc484c22b7e0f930ed9f6e8b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=cef98a9371e54d9594692383c4adc86f",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=2224f02c46874fb0b01ace8c156253f5",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=dd734167f9c94e698ab48b82dd9eb431",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=fc7be911e25a432fb407ae61c004a6ab",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=a91b5348001148d8bbe7105a707c5e5c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=97d693f9972f4d42987a2a1436c0b1da",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8eb51dc6f0714715a33e7a8529cb8ae1",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=a3a15f442b4c4d41a8e6aaf13372bac1",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b0231ccfab7c4c9592ac7045b95cbb90",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=058191d93fa34135a4ee9fef360fb53a",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c74204bfc41d4a4dae69d9f3734cf095",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=05ed4d435e5648058e27e84284aaceae",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=f473a6bbcabe4fd49199c2cef7205664",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=27f9449efbc34f64807a98ecbbcaa5ac",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d539778bb12e4ecbac2ca17d05239648",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b2664505d172485f997ff1e25d8720f1",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c651bf1e7d6145dc8b17296b700ab7ca",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=c86c65b53db04bb787d43e7888d9ce00",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=426cdc40077f4f488e972de716b39889",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b3f4017e08064dad818ba37ff20881af",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d798171c58f54584b56e9ff97f3a4014",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=39455dccb6c64576a0da0bd6ce1a5f9c",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=acd415e44e254cf4b490715e03bbfcbd",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=83306c7aa3074d0e9c904874a9ec2803",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e70e8ef10fb14e209407d3d305b9294d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=94f3bc3197bf4dbd9a3e17a506cf4be0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=541702aef4d04e42a0a5910870e10f80",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=aaea4f151d5d4d26a351963bc75ed06e",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b3a9cad2b448483897e17ed9d97e6c2b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=ed5af6c735ef41a7ae08c6f749996474",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=2274fe4c9c244f5f9fb4be94a422c652",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=47c26c84521245b2a70220f15d85f87d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9f9886d716f441368daf4b8cdefcb9e0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=faa4bb91565b48c58dadbb262866d401",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d35dbb40f3724555b7a65bc09d01bc35",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=e12f45aa060c498fbd9bf287a369b3fd",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=3c348dd78c534be383c48155d7c0156b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=8adfdb3d53a746ffaff45ed535cf75db",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=98078c5765e34a848f1fe074e9d9dc2b",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b94ee131a08b4360847ce974b8ecf588",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9d7c0185356744c0911adf48d8b58370",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=daa36b12dd1d4b2fb5e390edb13b50e1",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=dc0ee8d66f5742aaa2431a03a64e9d7d",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=24f37d8e23e748a6b06bc01dd0667796",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=380a36a066474d50b863b75a0e04f97a",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=d4c3672a8066413a92f8fc182b651301",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=328f363a3cf4496abceab11f5ad17ada",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=9e3746177735439daadd31b57fcbef09",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=31a96ed7fbef4ffdb053f42af51dcbd8",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=b18ce3573a0d4685b919813d08010602",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=38d1976e3edf4ac89905e27e05f19aa7",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=5403ad0fd01544dcbf7c82c8e9b85dc0",
"http://www.matweb.com/search/DataSheet.aspx?MatGUID=5909825d46994d9fa6a29a9ff71147a8"]

# Alloy name composition of alloy UTS YS %elongation

#Tensile Strength, Ultimate
#Tensile Strength, Yield 
#Elongation at Break

# for url in urls:
toFinds = ["Tensile Strength, Ultimate", "Tensile Strength, Yield"]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
results = []
i = 0
for url in urls:
    print(i)
    i+=1
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    # print("tbody" in html)
    # print(html)
    try:
        result['alloy'] = soup.find("table", class_="tabledataformat t_ableborder tableloose altrow").findChildren()[0].text.strip()
    except:
        result['alloy'] = "MISSING"
    for toFind in toFinds:
        if toFind in html:
            ut = soup.find(text = lambda t: toFind in t)
            result[toFind] = ut.find_next('td').a.text
        else:
            result[toFind] = "MISSING"

        if "Elongation at Break" in html:
            ut = soup.find(text = lambda t: "Elongation at Break" in t)
            result["Elongation at Break"] = ut.find_next('td').text
        else:
            result["Elongation at Break"] = "MISSING"
    try:
        curr = soup.find(text = lambda t: "Component Elements Properties" in t).parent.parent
        curr = curr.find_next('tr')
        result["Composition"] = {}
        while "%" in curr.text:
            children = curr.findChildren()
            result["Composition"][children[0].text.replace('\xa0', '')] = children[1].text
            curr = curr.find_next('tr')
    except:
        result["Composition"] = "MISSING"

    result['url'] = url
    results.append(result)

with open('data.json', 'w') as convert_file:
    convert_file.write(json.dumps(results))
