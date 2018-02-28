
class V2ApiProcessing:
  def get_coin_list(self, balance):
      coinList = []
      for key in balance.keys():
          if key != "errorCode" and key != "result" and key != "normalWallets" and key != "krw":
              coinList.append(key)

      return {"coinList":coinList}
