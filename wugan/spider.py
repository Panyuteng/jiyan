import requests
import execjs
import re
import json
import subprocess
execjs.get().name
print(execjs.get().name)
import datetime

if __name__ == '__main__':

    results = subprocess.check_output(['node', 'wugan.js']).decode('utf8').split('\n')
    print(results)
    challenge = results[0]
    callback_num = results[1]
    base_url = 'gt4.geetest.com'

    captcha_id = '99b142aaece96330d0f3ffb565ffb3ef'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    # 进行load请求 获取lot_number
    url = f'https://gcaptcha4.geetest.com/load?captcha_id={captcha_id}&challenge={challenge}&client_type=web&lang=zho&callback=geetest_{callback_num}'
    print(url)
    session = requests.session()
    r = session.get(url, headers=headers)
    print(r.text)
    data = json.loads(re.search(r'{".*}', r.text).group(0))
    print(data)
    lot_number = data['data']['lot_number']
    payload = data['data']['payload']
    process_token = data['data']['process_token']
    static_path = data['data']['static_path']
    # 2025-05-27T19:15:33.343239+08:00
    date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.343239+08:00')

    # 请求验证
    """
    lot_number = "lot_number";
    captchaId = "captchaId";
    datetime = "datetime";
    payload = "payload";
    staticPath = "staticPath"
    processToken = "processToken"
    """
    with open('wugan.js', 'r', encoding='utf8') as f:
        js_code = f.read().replace(f'"lot_number"', f'"{lot_number}"').replace(f'"captchaId"', f'"{captcha_id}"').replace(f'"datetime"', f'"{date_time}"').replace(f'"payload"', f'"{payload}"').replace(f'"staticPath"', f'"{static_path}"').replace(f'"processToken"', f'"{process_token}"')
    with open('wugan_tmp.js', 'w', encoding='utf8') as f:
        f.write(js_code)

    results = subprocess.check_output(['node', 'wugan_tmp.js']).decode('utf8').split('\n')
    print(results)

    # 点击请求验证
    """
    callback: geetest_1748344741517
    captcha_id:99b142aaece96330d0f3ffb565ffb3ef
    client_type:web
    lot_number:92c4a7d926254d6fa3712fa876f1ff27
    payload:AgFD8gWUUuHFx-XvpP7J2UCwVw3dPI8tuRJe1uW7ZFPytX1plngDmW1uyR2PYXUkstb0XbcQaL0XCkPJYz90njaCq7_K5kKRWx2TLhXz5Ho7r1Z50s0y9iKNmLfeMKVg50NEFK4bwn8FAhZWMkF-ZtgCtA1l5GLkPE4342jVjAWrU9Gqbxl6nMflvQtF0lEuDFXbGkdu__bHHp54skGLKsyMDO5wMOv7JdXgpckUuQN0SuHVjbpf9RqOy9CZWeTGtrgXjhLbzR2reVoYQBMg7sD47S1aNHYeG7y92XalfvTi2n3uCd_O1B1lb4q4d1zu-9Ja4UovK0yV18sJD0_Vcn-MqkMDDgg3tdZUuzHN_oA3TPcOlrX249hugBr_4IWDbGcDUOrOinacfeIMXmyRuO1p2TFmS32DZAm-X9Sl-EjHy4vbxsWg30HcMVmP2IlcqMv2uyItwATTErFz_2oLt4MdYAdkX4HKXXEwAEZp6A4rbMf2uKMTUBNLeNm7RHdZ7JfZ7_QLaC3ub_h2hGv8BX7jYegEjNZMcO00666elNQyq69acc447AbT-BMIFC8y1_uSdPIHdZpSblP7_FullbL1VeZQNb4W6mHfc-O_5mW9uf4fU0k-Uy0n3ubj9m452mppMwZCBUxF9ztmdkoZFo-lsK6YmX4yk_5BKj22ubKXkSzlvchcvYuHWksryx1Tep6KZi6b9n8gqhn8T70ulzZdUuNv9Flkf4ygtaxNrw6A9aBOsMz1TvBmk8vRKmVM3xZSTC-oYQaxRZDPg8yUFuleHj9aUPYKqBV0VR5JJ8wuhL97fSGIErfuOMIvLaxBXxImlwwnRhKN3U8ZNVdBa262Ww4fshrBMwlMMyfMQeYXcJEXVdxGIt9USdyUh26MU9b8mMedjlEArn9kwOCUOA==
    process_token:256f605b25640cf063fe9934299a270ed82068aab9cbc69cf51b5c1af88c0bfe
    payload_protocol:1
    pt:1
    w:675d2273fc664ffe3eef22ee9037f023e6d4d4de06a1267b7e836c57a291b0c68a28c6fc8256726cf6a45832f2e3cc7ea85add0900f1c74afc7986789eee82219bab4d7a17ff2ea42c3fb690dea139ec399bebe9afff4bfaa8b7a849a3a22910a85009c2c6c49267c381585afaa1a3274d3ef280a13cad0006155fc8c66ab6337cb4c87074f0f843fb99a180c42b7857268e21d205f30263ae082ae486055482c92747a3465c36ffc10f1a13708725c42d26464fc6f7456f1afaf6e51739003effe0be4ee7639a873d197cb113bbb1d23d355382631d695f454c6d3ab7f9e9bb45103c3a8e86184a9e02e128b3060d2c27315bef43e3708d68d0632258a95a314218af9b3d9091951a45370b1a7c26ec5840c84a9b33182556e3959320d3311505b2f6ef61539fc8cc90778776933e5d2d96b87b41cf05cb3322ab2c274482296943cae48e214fe133140ab25ba7f58c43c0a9e32630df52d6835ef6cbc15443b271fb842c5c7673879c4e538971f343825f396dc415570e85b93fbae19ae7e59c5f6c22ca5b1d5c683e3b820751d3a71382529b54641b1ceda01444d5c7e80826e056d480d5fb47e50dcfefc28f251b279c07097f43d3aacb2dcd90c780676fa5bd9e719ada2dd04061e1a574c8ed1ba4953755da53fbf6d199e36b0ee022a5d233f2fe259bd7798dfb8f87dcb02aee39c6d234c01e18a9691ab7921db7ba256d587cd8d16bd565cd8f65bbaec7c729377bbb0f35480c32dffa455cef6c255122e93a97e7c9f8b0c749674f7aaf9445
    """
    url = f'https://gcaptcha4.geetest.com/verify?callback=geetest_{results[1]}&captcha_id={captcha_id}&client_type=web&lot_number={lot_number}&payload={payload}&process_token={process_token}&payload_protocol=1&pt=1&w={results[2]}'
    r = session.get(url, headers=headers)
    print(r.text)
    data = json.loads(re.search(r'{".*}', r.text).group(0))
    lot_number = data['data']['lot_number']
    pass_token = data['data']['seccode']['pass_token']
    gen_time = data['data']['seccode']['gen_time']
    captcha_output = data['data']['seccode']['captcha_output']

    url = f'https://{base_url}/demov4/demo/login?captcha_id={captcha_id}&lot_number={lot_number}&pass_token={pass_token}&gen_time={gen_time}&captcha_output={captcha_output}'
    r = session.get(url, headers=headers)
    print(r.text)

    # 删除临时文件
    os.remove('challenge1_tmp.js')
