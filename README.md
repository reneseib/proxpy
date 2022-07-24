# proxpy
-------------------------------------
#### A Python wrapper for anonymous proxy requests
-------------------------------------

On instantiating the class <code>ProxyRequest</code>, a list of approx. 400 free, anonymous proxy socks5 servers gets loaded and saved to the instance.

On each request, a new server from the list if picked until all have been used once. Then it starts again from the beginning of the list. This should should ease scraping websites, as long as you don't flood the target server with requests. 

No liability or responsibility are taken for proper use, neither by the author nor by spys.one, therefore, use this tool and those servers with care and common sense.

```python
import proxpy

proxy_request = proxpy.ProxyRequest()

response = proxy_request.get("https://example.com")

```

Proxpy is still being developed.

This tool is based on the free proxy server list of to https://spys.one that you can find at https://spys.me/proxy.txt

Therefore, thanks and kudos to https://spys.one
