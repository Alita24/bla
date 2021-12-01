# "." to ","
c=input("insert ingredient ")
a=''
for i in c:
    if i=='-':
        i=','
    a+=i
print("ingredient list ",a)

# make list of bad ingredients
b=['Oxybenzone,', 'Benzophenone-1,', 'Benzophenone-8,', 'OD-PABA,', '4-Methylbenzylidene', 'camphor,', '3-Benzylidene', 'camphor,', 'nano-Titanium', 'dioxide,', 'nano-Zinc', 'oxide,', 'Octinoxate,', 'Octocrylene,', 'PABA,\tButylparaben,', 'Butyl-Methoxydibenzoylmethane,', 'Hexyldecanol', 'Methylparaben,', 'Dimethyl', 'Capramide,', 'Polyethylene,', 'Propylparaben,', 'Cetyl', 'Dimethicone','Butylcarbamate', 'Ethylhexyl methoxycinnamate']

d=a.split(",")
for i in d:
    for l in b:
        if i==l:
            print("wrong: ",l)
            break
print("ok")