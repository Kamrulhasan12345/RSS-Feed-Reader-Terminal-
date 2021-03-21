async def savetofile(string_to_save, filename):
  async with open(filename, 'w') as file:
    file = string_to_save
    return True