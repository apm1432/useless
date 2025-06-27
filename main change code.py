            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url:
                    #codewritten by pjvip for team also help @botupdatevip 
                    #also jion movie channel https://t.me/moviebyvip
                    url = url.replace('https://tencdn.classplusapp.com/', 'https://media-cdn.classplusapp.com/tencent/')
                    urlx = url 
                    headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-encoding': 'gzip',
                    'accept-language': 'EN',
                    'api-version': '35',
                    'app-version': '1.4.73.2',
                    'build-number': '35',
                    'connection': 'Keep-Alive',
                    'content-type': 'application/json',
                    'device-details': 'Xiaomi_Redmi 7_SDK-32',
                    'device-id': 'c28d3cb16bbdac01',
                    'host': 'api.classplusapp.com',
                    'region': 'IN',
                    'user-agent': 'Mobile-Android',
                    'webengage-luid': '00000187-6fe4-5d41-a530-26186858be4c',
                    'x-access-token': f'{token_cp}',
                    'X-CDN-Tag': 'empty'
                }
                     
                    

                    try:
# Send API request
                       response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={urlx}', headers=headers)
                    #print(response)
                       print(response.json())
                       url   = response.json()['url']
                    #urlp   = response.json()['url']
                    #url = urlp
                    except:

                                        
                      url = f'https://drmapijion-botupdatevip.vercel.app/api?url={urlx}'
                      print(url)
                      mpd = helper.get_mps_and_keys3(url) 
                      url = mpd
                      print(url)
                    
                        


            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or 'media-cdn-a.classplusapp.com' in url or "cpvod" in url or 'cpvideocdn' in url:
                    #codewritten by pjvip for team also help @botupdatevip 
                    #also jion movie channel https://t.me/moviebyvip
                    headers = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip',
                        'accept-language': 'EN',
                        'api-version': '35',
                        'app-version': '1.4.73.2',
                        'build-number': '35',
                        'connection': 'Keep-Alive',
                        'content-type': 'application/json',
                        'device-details': 'Xiaomi_Redmi 7_SDK-32',
                        'device-id': 'c28d3cb16bbdac01',
                        'host': 'api.classplusapp.com',
                        'region': 'IN',
                        'user-agent': 'Mobile-Android',
                        'webengage-luid': '00000187-6fe4-5d41-a530-26186858be4c',
                        'x-access-token': f'{token_cp}'
                    }
                    urlx = url
                    if '4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27' in url:
                        pattern = re.compile(r'https://videos\.classplusapp\.com/([a-f0-9]+)/([a-zA-Z0-9]+)\.m3u8')
                        match = pattern.match(url)
                        if match:
                            urlx = f"https://videos.classplusapp.com/b08bad9ff8d969639b2e43d5769342cc62b510c4345d2f7f153bec53be84fe35/{match.group(2)}/{match.group(2)}.m3u8"
                            url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={urlx}', headers=headers).json()['url']

                    if "testbook.com" in url or "classplusapp.com/drm" in url or "media-cdn.classplusapp.com/drm" in url:
                        url = url.replace("https://cpvod.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                        url = url.replace("https://cpvideocdn.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                        urlx = url
                        #params = (('url', f'{url}'), )
                        try:
                               url = f"https://drmapijion-botupdatevip.vercel.app/api?url={urlx}&token={raw_text4}" + urlx
                               
                               print(url)
                               mpd, keys = helper.get_mps_and_keys2(url)
                               url = mpd
                               keys_string = " ".join([f"--key {key}" for key in keys])
                               print(mpd)


                        except:
                               url = f"https://drmapijion-botupdatevip.vercel.app/api?url={urlx}&token={raw_text4}" + urlx
                               
                               print(url)
                               mpd, keys = helper.get_mps_and_keys2(url)
                               url = mpd
                               keys_string = " ".join([f"--key {key}" for key in keys])
                               print(mpd)  

                    else:

                        try: 
                            resp2 = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={urlx}', headers=headers).json() 
                            #url = resp2.json()['url']
                            #url = resp2['url'] 
                            if resp2['status'] ==  'ok':                          
                                 url = resp2['url']  

   
                        except:                               
                                url = f'https://drmapijion-botupdatevip.vercel.app/api?url={urlx}'
                                print(url)
                                mpd = helper.get_mps_and_keys3(url) 
                                url = mpd
                                print(url) 