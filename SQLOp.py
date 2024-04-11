import pandas as pd

# Sample DataFrames

datat = {'id':['001','002','003','004','005','006'],
        'city_name':['台北市','新北市','桃園市','台中市','台南市','高雄市'],
        'pop':[2631083, 4024539, 2255753, 2816741, 1878845, 2773401],
        'area':[271.7997, 2052.5667, 1220.9540, 2214.8968, 2191.6531, 2951.8524],}
dft = pd.DataFrame()

datas = {'no':['01','02','03','04'],
           'name':['apple','banana','cat','dog'],
           'sex':['girl','boy','girl','boy'],
           'city':['002','004','001','003']}
dfs = pd.DataFrame()

# Unary operators

# Selection (σ) operator
def select(df, condition):
    return df.query(condition).reset_index(drop=True)

# Projection (π) operator
def project(df, columns):
    return df[columns]

# Rename (ρ) operator
def rename(df, new_names):
    return df.rename(columns=new_names)

# Binary operators

# Cartesian Product (×) operator
def cartesian_product(df1, df2):
    return pd.merge(df1.assign(key=1), df2.assign(key=1), on='key').drop('key', axis=1)

# Set Union (∪) operator
def set_union(df1, df2):
    return pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)

# Set Difference (-) operator
def set_difference(df1, df2):
    return pd.concat([df1, df2, df2]).drop_duplicates(keep=False).reset_index(drop=True)

# User Interface

def load_database(data):
    # Load data from files or databases
    df = pd.DataFrame(data)
    print("Load done...")
    return df

def show_schema(df):
    print("Schema:")
    print(df.dtypes)


def set_naturalJoin(df1, df2):
    return pd.merge(df2, df1, how='inner', left_on='city', right_on='id')

def table(df):
    print(df)

def menu():
    print("1. Select (σ)")
    print("2. Project (π)")
    print("3. Rename (ρ)")
    print("4. Cartesian Product (×)")
    print("5. Set Union (∪)")
    print("6. Set Difference (-)")
    print("7. Natural Join ")
    print("8. Show Schema")
    print("9. Show table")
    print("10. Load Data")
    print("11. Quit")
    return int(input("Enter your choice: "))

def main():
    # Load database (not implemented)
    while True:
        choice = menu()
        if choice == 1:
            condition = input("Enter selection condition: ")
            print(select(dft, condition))
        elif choice == 2:
            columns = input("Enter columns to project (separated by comma): ").split(',')
            print(project(dft, columns))
        elif choice == 3:
            new_names = dict(input("Enter column rename mapping (column:new_name): ").split(':') for _ in range(len(dft.columns)))
            print(rename(dft, new_names))
        elif choice == 4:
            print(cartesian_product(dft, dfs))
        elif choice == 5:
            print(set_union(dft, dfs))
        elif choice == 6:
            print(set_difference(dft, dfs))
        elif choice == 7:
            print(set_naturalJoin(dft,dfs))
        elif choice == 8:
            show_schema(dft)
            show_schema(dfs)
        elif choice == 9:
            table(datat)
            table(datas)
        elif choice == 10:
            dft = load_database(datat);
            dfs = load_database(datas);
        elif choice == 11:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
