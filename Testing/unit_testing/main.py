
def test_calculate_total_empty_list():
    assert calculate_total([]) == 0

def test_calculate_single_product():
    products = [{"name": "notebook", "price": 5}]
    assert calculate_total(products) == 5

def test_calculate_total_multiple_products():

    products = [
        {"name": "notebook", "price": 5},
        {"name": "pen", "price": 2},
        {"name": "eraser", "price": 1}
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 8


def calculate_total(products):
    total=0
    for produc in products:
        total += produc["price"]
    return total


def test_calculate_total_empty_list():
    print(" testing ")
    assert calculate_total([])==0

def test_calculate_single_products():
    
    products=[{
          "name":"notebook","price":5
     }]
    print(calculate_total(products))
    assert calculate_total(products)==5



if __name__ == "__main__":
      
      test_calculate_total_multiple_products()