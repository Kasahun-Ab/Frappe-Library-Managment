import frappe
from frappe import _

# Book API Methods
@frappe.whitelist(allow_guest=True)
def create_book(title, isbn, published_date, author):
    """Create a new Book entry in the database"""
    if frappe.db.exists("Book", isbn):
        frappe.throw(_("Book with ISBN {} already exists").format(isbn))

    book = frappe.new_doc("Book")  # Create a new Book document
    book.title = title
    book.isbn = isbn
    book.published_date = published_date
    book.author = author
    book.insert()  # Save the new book in the database
    return book

@frappe.whitelist(allow_guest=True)
def get_books():
    """Retrieve all Books"""
    return frappe.get_all('Book', fields=['name', 'title', 'author', 'isbn'])


@frappe.whitelist()
def get_book_details(isbn):
    """Retrieve Book by ISBN"""
    # Check if the book exists in the database
    if not frappe.db.exists("Book", {"isbn": isbn}):
        frappe.throw(_("Book with ISBN {} not found").format(isbn))  # If not, throw an error

    # Fetch the book document
    book = frappe.get_doc("Book", {"isbn": isbn})
    
    # Return the book as a dictionary
    return book.as_dict()






@frappe.whitelist()
def update_book(isbn, title=None, published_date=None, author=None):
    """Update an existing Book's details"""
    # Check if a book with the given ISBN exists
    book = frappe.db.get_value("Book", {"isbn": isbn}, ["name"])  # Get the 'name' of the book using the ISBN
    
    if not book:
        # If no book is found, raise an error
        frappe.throw(_("Book with ISBN {} not found").format(isbn))  # Throw error if book doesn't exist

    # Fetch the book document using its 'name' (book's unique ID in Frappe)
    book_doc = frappe.get_doc("Book", book[0])

    # Update the book's details if any new values are provided
    if title:
        book_doc.title = title
    if published_date:
        book_doc.published_date = published_date
    if author:
        book_doc.author = author
    
    # Save the updated book
    book_doc.save()
    
    # Return the updated book as a dictionary
    return book_doc.as_dict()





@frappe.whitelist()
def delete_book(isbn):
    """Delete a Book from the database"""
    
    # Check if the book exists using the ISBN value
    book = frappe.db.get_value("Book", {"isbn": isbn}, ["name"])

    # If no book is found, raise an error with a specific message
    if not book:
        frappe.throw(_("Book with ISBN {} not found").format(isbn))
    
    # Delete the book document using the 'name' field (unique ID)
    frappe.delete_doc("Book", book[0])
    
    # Return a success message
    return _("Book with ISBN {} has been successfully deleted").format(isbn)


# Member API Methods
@frappe.whitelist(allow_guest=True)
def create_member(name, membership_id, phone, email):
    """Create a new Member entry in the database"""
    if frappe.db.exists("Member", membership_id):
        frappe.throw(_("Member with Membership ID {} already exists").format(membership_id))

    member = frappe.new_doc("Member")
    member.name = name
    member.membership_id = membership_id
    member.phone = phone
    member.email = email
    member.insert()
    return member
@frappe.whitelist()
def get_members():
    """Retrieve all members from the database"""
    members = frappe.get_all("Member", fields=["name", "membership_id", "phone", "email"])
    if not members:
        frappe.throw(_("No members found"))
    return members


@frappe.whitelist(allow_guest=True)
def get_member_details(membership_id):
    """Retrieve details of a member by their Membership ID"""
    member = frappe.get_doc("Member", {"membership_id": membership_id})
    if not member:
        frappe.throw(_("Member with Membership ID {} not found").format(membership_id))
    return member.as_dict()



@frappe.whitelist(allow_guest=True)
def update_member(membership_id, name=None, phone=None, email=None):
    """Update the details of an existing member"""
    # Check if the member exists
    if not frappe.db.exists("Member", {"membership_id": membership_id}):
        frappe.throw(_("Member with Membership ID {} does not exist").format(membership_id))

    # Fetch the member document
    member = frappe.get_doc("Member", {"membership_id": membership_id})

    # Update fields if new values are provided
    if name:
        member.name = name
    if phone:
        member.phone = phone
    if email:
        member.email = email

    # Save the updated member document
    member.save()
    return member.as_dict()

    
@frappe.whitelist()
def delete_member(membership_id):
    """Delete a Member from the database"""
    if not frappe.db.exists("Member", membership_id):
        frappe.throw(_("Member with Membership ID {} does not exist").format(membership_id))

    frappe.delete_doc("Member", membership_id)
    return _("Member deleted successfully")


# Loan API Methods
@frappe.whitelist(allow_guest=True)
def create_loan(member, book, loan_date, return_date):
    """Create a new Loan entry"""
    loan = frappe.new_doc("Loan")
    loan.member = member
    loan.book = book
    loan.loan_date = loan_date
    loan.return_date = return_date
    loan.insert()
    return loan

@frappe.whitelist(allow_guest=True)
def get_loan(loan_id):
    """Retrieve Loan details by Loan ID"""
    if not frappe.db.exists("Loan", loan_id):
        frappe.throw(_("Loan with ID {} does not exist").format(loan_id))

    loan = frappe.get_doc("Loan", loan_id)
    return loan.as_dict()

# @frappe.whitelist()
# def update_loan(loan_id, member=None, book=None, loan_date=None, return_date=None):
#     """Update an existing Loan's details"""
#     if not frappe.db.exists("Loan", loan_id):
#         frappe.throw(_("Loan with ID {} does not exist").format(loan_id))

#     loan = frappe.get_doc("Loan", loan_id)
#     if member:
#         loan.member = member
#     if book:
#         loan.book = book
#     if loan_date:
#         loan.loan_date = loan_date
#     if return_date:
#         loan.return_date = return_date
#     loan.save()
#     return loan

# @frappe.whitelist()
# def delete_loan(loan_id):
#     """Delete a Loan from the database"""
#     if not frappe.db.exists("Loan", loan_id):
#         frappe.throw(_("Loan with ID {} does not exist").format(loan_id))

#     frappe.delete_doc("Loan", loan_id)
#     return _("Loan deleted successfully")
