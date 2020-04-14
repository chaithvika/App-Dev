from solution import LRUCache

def main():
	test = LRUCache(3)
	test.put(1,"one")
	test.put(2,"two")
	test.put(3,"three")
	assert test.cache == {1:"one", 2:"two", 3:"three"}
	test.put(3, "four")
	assert test.cache == {1:"one",2:"two",3:"four"}
	test.put(4, "five")
	test.put(5, "six")
	assert test.cache == {3:"four", 4:"five", 5:"six"}
	print("Yayy! All the assert statements are passed.")

if __name__ == "__main__":
	main()