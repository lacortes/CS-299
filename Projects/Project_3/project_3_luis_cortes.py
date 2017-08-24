# /usr/local/bin/python3
# Luis Cortes
# CS 299
# Project 3

PIZZA_SIZES = {"10": 10.99, "12": 12.99, "14": 14.99, "16": 16.99}
CRUST_CHOICES = {"1": 0.00, "2": 1.00, "3": 2.00}
COUPONS = {"Holiday10": 0.1, "Winter20": 0.2, "VIPmax": 0.25}
ORDER = []


def get_size():
    tries = 3

    # Give user 3 tries to enter correct choice
    print("##########################")
    print("#         Sizes          #")
    print("#************************#")
    print("#       10 inches        #")
    print("#       12 inches        #")
    print("#       14 inches        #")
    print("#       16 inches        #")
    print("##########################")
    print()
    while tries > 0:

        user_size = input("Enter pizza size: ")

        if user_size in PIZZA_SIZES:  # Check if input is valid
            ORDER.append(user_size)  # Update order details
            return PIZZA_SIZES[user_size]
        tries -= 1
    else:
        print("Very Sorry")
        return -1


def get_crust():
    print("##########################")
    print("#        Crusts          #")
    print("#************************#")
    print("#   (1) Hand-tossed     #")
    print("#   (2) Thin-crust      #")
    print("#   (3) Deep-dish       #")
    print("##########################")

    crust = input("Choose crust: ").replace(" ", "")

    # Return corresponding fee
    if len(crust) > 0 and crust in CRUST_CHOICES:
        print(crust)
        # Update order details
        if crust == "1":
            ORDER.append("HAND")
        elif crust == "2":
            ORDER.append("THIN")
        elif crust == "3":
            ORDER.append("DEEP")

        return CRUST_CHOICES[crust]

    # Wrong choice entered
    ORDER.append("HAND")
    return CRUST_CHOICES["1"]


def apply_discount():
    code = input("COUPON CODE: ").replace(" ", "")

    if code in COUPONS:
        return COUPONS[code]  # Return corresponding code
    return 0.00  # No discount


def cost(size, extra, discount):
    total = size + extra
    dis = total * discount
    ORDER.append(dis)
    return total - dis


def main():
    print("+========================+")
    print("+       CPP Pizza        +")
    print("+========================+")

    size = get_size()

    if size == -1:  # Check if valid size
        print("Goodbye!")
        exit()

    crust = get_crust()
    discount = apply_discount()
    total = cost(size, crust, discount)

    print("**********************")
    print("*      RECEIPT       *")
    print("*--------------------*")
    print(" Size: {0}\"     ${1}".format(ORDER[0], size))
    print(" Crust: {0}   ${1:3.2f}".format(ORDER[1], crust))
    print(" Discount:     ${0:3.2f}".format(ORDER[2]))
    print("*---------------------*")
    print(" Total: ${0:3.2f}".format(total))

    print()
    print("***Thank You For Ordering At CPP Pizza***")
if __name__ == "__main__":
    main()

# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 15
# Enter pizza size: 11
# Enter pizza size: 17
# Very Sorry
# Goodbye!

# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 17
# Enter pizza size: 16
# ##########################
# #        Crusts          #
# #************************#
# #   (1) Hand-tossed     #
# #   (2) Thin-crust      #
# #   (3) Deep-dish       #
# ##########################
# Choose crust: h
# COUPON CODE: Winter20
# **********************
# *      RECEIPT       *
# *--------------------*
#  Size: 16"     $16.99
#  Crust: HAND   $0.00
#  Discount:     $3.40
# *---------------------*
#  Total: $13.59
#
# ***Thank You For Ordering At CPP Pizza***

# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 12
# ##########################
# #        Crusts          #
# #************************#
# #   (1) Hand-tossed     #
# #   (2) Thin-crust      #
# #   (3) Deep-dish       #
# ##########################
# Choose crust: 3
# 3
# COUPON CODE:
# **********************
# *      RECEIPT       *
# *--------------------*
#  Size: 12"     $12.99
#  Crust: DEEP   $2.00
#  Discount:     $0.00
# *---------------------*
#  Total: $14.99
#
# ***Thank You For Ordering At CPP Pizza***


# Test 4
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 14
# ##########################
# #        Crusts          #
# #************************#
# #   (1) Hand-tossed     #
# #   (2) Thin-crust      #
# #   (3) Deep-dish       #
# ##########################
# Choose crust: 2
# 2
# COUPON CODE: VIPmax
# **********************
# *      RECEIPT       *
# *--------------------*
#  Size: 14"     $14.99
#  Crust: THIN   $1.00
#  Discount:     $4.00
# *---------------------*
#  Total: $11.99
#
# ***Thank You For Ordering At CPP Pizza***

# Test 5
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 10
# ##########################
# #        Crusts          #
# #************************#
# #   (1) Hand-tossed     #
# #   (2) Thin-crust      #
# #   (3) Deep-dish       #
# ##########################
# Choose crust: 1
# 1
# COUPON CODE: Holiday10
# **********************
# *      RECEIPT       *
# *--------------------*
#  Size: 10"     $10.99
#  Crust: HAND   $0.00
#  Discount:     $1.10
# *---------------------*
#  Total: $9.89
#
# ***Thank You For Ordering At CPP Pizza***


# Test 6
# ----------------------------------------------------------------------------------------------------------------------
# +========================+
# +       CPP Pizza        +
# +========================+
# ##########################
# #         Sizes          #
# #************************#
# #       10 inches        #
# #       12 inches        #
# #       14 inches        #
# #       16 inches        #
# ##########################
#
# Enter pizza size: 12
# ##########################
# #        Crusts          #
# #************************#
# #   (1) Hand-tossed     #
# #   (2) Thin-crust      #
# #   (3) Deep-dish       #
# ##########################
# Choose crust: 3
# 3
# COUPON CODE:
# **********************
# *      RECEIPT       *
# *--------------------*
#  Size: 12"     $12.99
#  Crust: DEEP   $2.00
#  Discount:     $0.00
# *---------------------*
#  Total: $14.99
#
# ***Thank You For Ordering At CPP Pizza***