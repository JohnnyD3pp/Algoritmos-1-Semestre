dias = float(input('Quantos dias você ficou no hotel? '))

diaria = 300.00 * dias

mais15 = dias * 22.50
igual15 = dias * 56.00
menos15 = dias * 88.00


if dias > 15:
    print(f'O valor a ser pago é de: ${diaria + mais15: .2f}')
elif dias < 15:
    print(f'O valor a ser pago é de: ${diaria + menos15: .2f}')
else: 
    print(f'O valor a ser pago é de: ${diaria + igual15: .2f}')

#ou desta forma:

#if dias > 15:
   # taxa = 22.50
#elif: dias < 15
   # taxa = 88.00
#else:
   # taxa = 56.00

#conta = (300 + taxa) * dias

#print(f'O valor da conta é de: {conta: .2f}')