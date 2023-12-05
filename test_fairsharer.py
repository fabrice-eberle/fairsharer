from main import *

# def unit_tester():  
#     assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90] , "It worked"
  
# if __name__ == "__main__":  
#     unit_tester()  
#     print("Test passed")  

def test_fairsharer():
    result = fair_sharer([0, 1000, 800, 0], 2)
    expected = [100, 890, 720, 90]
    assert result == expected
    
def test_fairsharer_2():   
    result = fair_sharer([0, 1000, 800, 0], 1) 
    expected = [100, 800, 900, 0]
    assert result == expected

