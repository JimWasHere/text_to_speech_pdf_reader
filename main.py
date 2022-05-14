from pdf_reader import PdfReader

pdf = PdfReader("books/06. The Magic Shop Author H. G. Wells.pdf")
lst = pdf.page_numbers()
lst1 = lst.copy()
keep_going = True
while keep_going:
    string = " ".join([str(x) for x in lst1])
    print(f"Please pick a page from your file to start reading: \n\n{string}\n")
    pg = input("Which page would you like me to read? Choose from the list or type 'quit' to exit: ")
    if pg.lower() == "quit":
        keep_going = False
    else:
        try:
            pg = int(pg)
            if pg in lst:
                print("processing.....please....wait.....")
                lst1[pg - 1] = "*"
                pdf.read_out_loud(pg)

            else:
                print("Invalid entry, please choose from the list")
        except ValueError:
            print("That's not a number")



