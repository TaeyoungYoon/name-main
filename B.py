import A
#import되었으므로
#importA top level in A.py 출력
#A.py is imported 출력
#if문에서 name이 달라졌기 떄문에 A가 main이 아니다

print("top level in B.py")

if __name__ == "__main__" :
	print("B.py is executing directly")
else :
	print("B.py is imported")
