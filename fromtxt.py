import parser

async def parsefile(file):
  urls = []
  async with open(file, 'r') as file:
    for url in file:
      urls += url.split('\n')
    urls = list(filter(None, urls))
    return await [await parser.parse(url) for url in urls]