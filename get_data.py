import requests
import re
import csv

# 注册后的cookie
headers = {
    "cookie": "_vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=JCCA6FF5F3574197BCD81D15DB2208A89; _vwo_ds=3%241676514342%3A13.44901324%3A%3A; _vwo_uuid_v2=D46C475B87AE611444F39232D1E921D16|fc447c6f13a28b3814161d1b70f696b5; sgID=614b610a-79aa-f5b5-fd0c-dbb211556c64; _gcl_au=1.1.1207247122.1676514344; _gid=GA1.2.1340585573.1676514345; _fbp=fb.1.1676514344865.685162807; sw_reg_params=action%3Dcountries; _ga_XGRRHHKH0P=GS1.1.1676514343.1.1.1676514367.0.0.0; _ga=GA1.2.1041760065.1676514344; _uetsid=371f42b0ada111eda6e0a3a2f5f57330; _uetvid=371f5540ada111ed9d363f38c5a6d440; .DEVICETOKEN.SIMILARWEB.COM=gNklw1qcHGFMiw26UwkEk6Udd4NSG0KI; .SGTOKEN.SIMILARWEB.COM=q-YLQcxXOjvlCneIPzaOeI-D7cMUyWbYEkwOmgDmsAi7yf-_KEv3pJVZ4QAFvLzR11Emc8bBsi9Ji3y4mg_YLhAj7sU5JDhLiW68F3sCsMsbhTKLFc6cTMb5ZlL1jLOs2PX0XqURB4jIifQTI3eZoMLLnrDqmETdZxiyVNiFlE8ZfqGfoCjsu4uhUCTiypww3Bybuk0N_PbH88DqJGalt7VeJk9u3rjuDMvomRl_QMeV0y9W6yn0XR0OvkK11nDDZ9lePFCm3Lu8iu_q4wmox-981lTzedi_0HtaLMjIa-FOJWcuks6ZgRenmN0_lhq62c8RpU45WAj3H0Ud8fAXrI4-8YQ2Z-XBUhZVPw7CCSzHHRmgAUf64y18Kp6hw992NpEj6fDwaj67JeYpj-J3U0ixpx2OecXAH_fsSPnr8wda0Ga8P4YWpOLdPePs01Ke; locale=zh-cn; RESET_PRO_CACHE=False; ln_or=eyIzNjUwNCI6ImQifQ%3D%3D; _BEAMER_USER_ID_zBwGJEbQ32550=2711f2f1-f481-4716-86ec-fef99385d350; _BEAMER_FIRST_VISIT_zBwGJEbQ32550=2023-02-16T02:26:45.973Z; vv_visitor_id=vqZBr9prevSn8bIpdjLIDpSfACS0qkQ; fsrndidpro=false; _abck=A951A5E226D4680FCE2C2A08531D3B40~0~YAAQPKo4F6yW4DCGAQAA9F9xWgn78HSg9KTmGkFz+FW9wdrlm+QEEMHqFHpNVlagzqF37gwKqBWd1RhncQRe59FlWJPKqO+IyFLVZaTfwABvgVazOugQwHHC67ERf2ZbSRFTc8duW9HcQlQz0GSihvUKf2g8bpfDh3O6yB5+uWrO+ZbApKEz+4KeLT6WzvxypLnUKr6GfHcrBIMQfN5Un1GiNyGpkbRiKdU6lFhfgu3yfrgGZPMkZE2/Srg6ib8phmiCZiwBlSIvV1NfhrWeo4WDPOuAGEYgVHSnTtIAueZpPZBryta+kZszpCI8MDDh7wqeXSy7qYJXiN5oHBa/gxif1xdeLTEofEQgoG7Y1YKOKnfcFel2QxHZUdJBLhl2jlz4JqCnVraoNDTsthiJODyC3zxSaGoSMeVXv7g=~-1~-1~-1; ak_bmsc=94FD29CAB4938E23DCCE89981D0E60E3~000000000000000000000000000000~YAAQPKo4F62W4DCGAQAA9F9xWhKNH0YckP5KnkW0EeO4e3pbF6rogFapdVNZkp5x8AS988xBXWEwvTBvVbjbxp3bAiykX/fv4aqH6cVW7TRVzPk63nBoUR67j42ohjFQwHIAtlj0l3pl9dE6CUyPJj1jhW7bwBQwzT3VPxvQk5IgAwhIq9ec1MQn4HJs8KPq840pjlewws0KzDkXclUqxfOoKbsNERBFyQa6979hjCu135Inuxcr1qn6UJ2wncrmaDgB6PB6vJTh4pEaxceoICqiAVGnyGLFyirn28gTlf3b6AnPKF189vtuuabFmmgDSddi8Any2clprfBNGE0XwSnzNrBc+1DBQzDFD5D0BeDQwjV8HgtpbDSNkUSp20Xv1iYUGxLkgYEYx4qkZF1w; bm_sz=025FAC11A2B224F79765991BB30373DC~YAAQPKo4F66W4DCGAQAA9F9xWhI2iimbHRrnM/c9suGCUp5a/m521YMUwg/P01JzvejmBjClnxvmKu1jPRu33dMk1tPt37bjGS0cyS06GSty80Xmmhujei/RFY71Mh5b+UBXWo9p+4R3G4kbE1xIKEAs6TfdYPi3JfMSjDzIpmRNFBMneh4lGWnlhuAqtNzVkOJCqf6MAbqngc8p++IQzIRBLG9vNDHFcB9GJBb/8Npux9jvk27/y+xVIsxeJDs83QajaN74XHuePdcOFp8i/smzlRWI2pmy0N7oZATcoK0KalMxt5GT~3290434~3424568; bm_sv=588C86A1C135AAAB3B54892C2E82B138~YAAQtmABF0mAY1mGAQAA4o2SWhJk9xbkTJjzkyLiDEB9tGHtF7ogk84XYTbdbElMASh699zWZ3mxv6xxhMSdummjMDR8P+dFO8QAFZ5PK63u5k/SyCeksRmZwbX449AlnfQ9Pcwtvjj1OyJuLyG+9VgOa9QpPYWrBcLq0D4Pn0J2ICE/D1pMT02pVOLNMiwuqtoPZLD4mGqKzI724twdM8ou/sg7bMs/1nw70MetywlO7d3133MUENsQLv8lxPyyPFUzBQ==~1; _pk_id.1.fd33=acbcdd8e1a71f9aa.1676514344.; _pk_ses.1.fd33=1; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%2216187813%22%2C%22%24device_id%22%3A%20%22186580ac09d659-070b08ff6797fe-74525476-151800-186580ac09efab%22%2C%22sgId%22%3A%20%22614b610a-79aa-f5b5-fd0c-dbb211556c64%22%2C%22site_type%22%3A%20%22Pro%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22session_id%22%3A%20%221d1fc363-a1fc-45fe-83d6-ead6583efd91%22%2C%22session_first_event_time%22%3A%20%222023-02-16T14%3A13%3A21.079Z%22%2C%22url%22%3A%20%22https%3A%2F%2Fpro.similarweb.com%2F%23%2Fdigitalsuite%2Fwebsiteanalysis%2Fhome%22%2C%22language%22%3A%20%22zh-cn%22%2C%22sw_extention%22%3A%20false%2C%22last_event_time%22%3A%201676556801087%2C%22is_sw_user%22%3A%20false%2C%22mode%22%3A%20%22single%22%2C%22domain%22%3A%20%22google.com%22%2C%22is_small_site%22%3A%20false%2C%22is_ga_connected%22%3A%20false%2C%22first_time_visitor%22%3A%20false%2C%22page_id%22%3A%20%22Competitive%20Research-Website%20Analysis%2FHome-Analyze%20Websites%22%2C%22email%22%3A%20%22201906061601%40zjut.edu.cn%22%2C%22%24user_id%22%3A%20%2216187813%22%2C%22ui_generation%22%3A%20%2220230216.41793.577254a%22%2C%22subscription_id%22%3A%20%2247529692%22%2C%22base_product%22%3A%20%22Digital%20Marketing%20Intelligence%20Trial%22%2C%22user_id%22%3A%2016187813%2C%22account_id%22%3A%2010000041%2C%22app_mode%22%3A%20null%2C%22section%22%3A%20%22Competitive%20Research%22%2C%22sub_section%22%3A%20%22Website%20Analysis%2FHome%22%2C%22sub_sub_section%22%3A%20%22Analyze%20Websites%22%2C%22entity_id%22%3A%20%22%22%2C%22entity_name%22%3A%20%22%22%7D; vv_session_id=SAjuc0zDUOmVg2kE71Bet6LfNZIEtglOSEpgrYg4aejzIJ; _BEAMER_FILTER_BY_URL_zBwGJEbQ32550=true; _ots=1.1676556803857.1676556803857.1676556803857; _otui=494377837.1676514406067.1676554418939.1676556803857.4.5.217068; _otpe=https%3A%2F%2Fpro.similarweb.com%2F%23%2Fdigitalsuite%2Fwebsiteanalysis%2Fhome; __q_state_9u7uiM39FyWVMWQF=eyJ1dWlkIjoiM2MwYTkyOWItMGY2MS00MDY3LTllZGMtMDJhM2JjM2RiNzEwIiwiY29va2llRG9tYWluIjoic2ltaWxhcndlYi5jb20iLCJtZXNzZW5nZXJFeHBhbmRlZCI6ZmFsc2UsInByb21wdERpc21pc3NlZCI6ZmFsc2UsImNvbnZlcnNhdGlvbklkIjoiMTA3NTU1MDc2NDE3OTI2ODc3OCJ9"
}

#爬取的网站
WebList=['hao123.com', 'weibo.com', 'zhihu.com', 'google.com', 'cnblogs.com', 'jianshu.com', 'sogou.com', '163.com',
 'google.cn', 'google.com.hk', 'sohu.com', 'baigoogledu.com', 'github.com', 'yisou.com', 'soso.com', 'yodao.com',
 'cn.bing.com', 'youdao.com', 'msn.cn', 'cloud.tencent.com', 'jb51.net', 'zhongsou.com',
 'bilibili.com', 'csdn.net', '52pojie.cn', 'movie.douban.com', 'youtube.com', 'ddrk.me',
 'acfun.cn', 'dmzj.com', 'manhuagui.com', 'dm5.com', 'nfyingshi.com', 'pkmp4.com',
 '36dm.com', 'miobt.com', 'btbtt13.com', 'gimy.app', 'soman.com', 'zimuxia.cn', 'fantia.jp', 'kuaikanmanhua.com', 'copymanga.org', '555dy1.com',
 '1kkk.com', 'yyds.fans', 'zzzfun.com', 'ai66.ccdouban.com', 'downsub.com', 'juzikong.com', '4399dmw.com', 'youku.com',
 'hdpianyuan.com', 'calmlab.com', 'upanso.com', 'zcool.com.cn', 'giphy.com', 'anjixiong.com',
 'colorhunt.co', '6090yy.org', 'xingzuo360.cn', 'mjutv.cn',
 'daofire.com', 'hanfan.cc', 'gimy.tv', 'china95.net', 'lizhi.fm', '365j.com', 'cashl.edu.cn', 'infoteca.it',
 'hkbulib.hkbu.edu.hk', 'library.nao.ac.jp', 'cnki.net', 'unibooks.com.au', 'isbn.org.cn', 'yidu.edu.cn',
 'email.whu.edu.cn', 'gzky.edu.cn', 'duxiu.com', 'bliss.chubu.ac.jp', 'library.help.edu.my',
 'library.iiita.ac.in', 'library.pes.edu', 'webopac.uksw.edu', 'lib3.msu.ac.th', 'openreview.net', 'paperswithcode.com',
 'ieeexplore.ieee.org', 'aaai.org', 'sigsac.org', 'computer.org', 'huggingface.co', 'machinelearningmastery.com',
 'ijcai.org', 'deepai.org', 'notion.so', 'raw.githubusercontent.com',
 'usenix.org', 'jmlr.org', 'techtarget.com', 'connectedpapers.com', 'leetcode.com', 'c2.com', 'splashcon.org',
 'dreamsongs.com', 'research.google', 'matplotlib.org', 'ingentaconnect.com', 'superuser.com', 'openai.com']

for domain in WebList:
    req = requests.get(
        "https://pro.similarweb.com/widgetApi/WebsiteGeographyExtended/GeographyExtended/Table?includeSubDomains=true"
        "&keys=" + domain + "&from=2022%7C12%7C01&to=2023%7C01%7C31&country=999&webSource=Total&isWindow=false"
                            "&timeGranularity=Monthly&page=1&pageSize=200",
        headers=headers)
    page = req.text

    # 国家列表
    patternCountry = "\"text\":\"(.+?)\","
    countryList = re.findall(patternCountry, page)

    # 占比列表
    patternShare = "\"Share\":(.+?),"
    shareList = re.findall(patternShare, page)

    # 整合结果
    result = []
    for i in range(len(countryList)):
        result.append([countryList[i], shareList[i]])

    with open('./data/' + domain + '.csv', "w", encoding='utf-8', newline="") as s:
        w = csv.writer(s)
        for row in result:
            w.writerow(row)