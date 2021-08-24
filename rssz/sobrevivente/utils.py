from sobrevivente.models import Item, Inventario


def encontrar_item(nome):

    try:
        item = Item.objects.get(nome=nome)
    except:
        return None

    return item


def encontrar_inventario(item, sobrevivente):

    try:
        inventario = Inventario.objects.get(
            item=item, sobrevivente=sobrevivente)
    except:
        return None

    return inventario


def adicionar_inventario(sobrevivente, inventarios):

    if inventarios == None:
        return

    for i in inventarios:

        try:
            item = encontrar_item(i['item'])
            quantidade = i['quantidade']

            inventario = encontrar_inventario(item, sobrevivente)

            if inventario == None:
                inventario = inventario.objects.create(
                    item=item,
                    quantidade=quantidade,
                    sobrevivente=sobrevivente
                )
            else:
                inventario.quantidade = inventario.quantidade + quantidade
                inventario.save()

        except:
            pass
