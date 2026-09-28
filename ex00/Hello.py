ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")

# ft_tuple[1] = "France!" // error
# tupleは変更ができない型なので、一度listに変換してから変更する
temp_list = list(ft_tuple)
temp_list[1] = "France!"
ft_tuple = tuple(temp_list)

# setは順序を保証しないので、Paris!が先に表示される場合もある
ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
