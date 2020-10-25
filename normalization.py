from sklearn.preprocessing import MinMaxScaler
iniData = [[1200000, 31],[200000,41],[300000, 21],[9000000, 51]]

panggilFungsiScaler = MinMaxScaler()
print(panggilFungsiScaler.fit(iniData))