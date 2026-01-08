import getpass, sys

def pin_input(prompt='PIN: '):
    try: return getpass.getpass(prompt)
    except: return input(prompt)
def auth(pin, tries=3):
    for i in range(tries):
        if pin_input()==pin: return True
        print(f"Incorrect ({tries-i-1} left)")
    return False
def money(x): return f"${x:,.2f}"
def main():
    pin="1234"; bal=1000.0
    if not auth(pin): print("Blocked"); return
    while True:
        print("\n1)Balance 2)Withdraw 3)Deposit 4)Change PIN 5)Exit")
        c=input("Choose: ").strip()
        if c=='1':
            print("Balance:", money(bal))
        elif c=='2':
            a=input("Withdraw amount: ")
            try:
                v=float(a); 
                if v<=0: raise ValueError
                if v>bal: print("Insufficient funds")
                else: bal-=v; print("Dispensed", money(v))
            except: print("Invalid amount")
        elif c=='3':
            a=input("Deposit amount: ")
            try:
                v=float(a); 
                if v<=0: raise ValueError
                bal+=v; print("Deposited", money(v))
            except: print("Invalid amount")
        elif c=='4':
            o=pin_input("Current PIN: ")
            if o==pin:
                n=pin_input("New PIN: "); m=pin_input("Confirm PIN: ")
                if n and n==m: pin=n; print("PIN changed")
                else: print("PIN mismatch")
            else: print("Incorrect PIN")
        elif c=='5':
            print("Goodbye"); return
        else: print("Invalid option")
if __name__=="__main__":
    try: main()
    except KeyboardInterrupt: sys.exit("\nGoodbye.")
