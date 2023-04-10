def script():

    import json

    from core.models import Department, Property, InventoryList, MOL
    with open('core/info.json', encoding='utf-8') as file:
        request = json.loads(file.read())

    for corp in request:
        for item in corp:
            print(item)
            print(item['cabinet '])
            if not Department.objects.filter(cabinet=item['cabinet ']):
                department = Department(cabinet=item['cabinet'], organiztion_id=1).save()
            if not MOL.objects.filter(department_cabinet=item['cabinet']):
                MOL(department=department).save()
            if not Property.objects.filter(name=item['name']):
                property = Property(name=item['name']).save()
            if item.get('invent_num') is not None and not InventoryList.objects.filter(invent_num=item.get('invent_num')):
                InventoryList(property=Property.objects.filter(name=item['name']), MOL=MOL.objects.filter(department_cabinet=item['cabinet']),
                                             description=item.get('description', ''), invent_num=item.get('invent_num', ''), amount=1).save()

            elif inv := InventoryList.objects.filter(property_name=item['name'], MOL_department_cabinet=item['cabinet'],
                                                     description=item.get('description', '')):
                inv.amount += 1
                inv.save()

            else:
                invent_list = InventoryList.objects.filter(invent_num=item.get('invent_num'))
                invent_list.amount += 1
                invent_list.save()


