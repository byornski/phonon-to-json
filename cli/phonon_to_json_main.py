import argparse

AP = argparse.ArgumentParser(prog="phonon_to_json", description="Takes a CASTEp .phonon file and outputs a .json file readable by https://henriquemiranda.github.io/phononwebsite/phonon.html")
AP.add_argument("filename")
AP.add_argument("name")
AP.add_argument("formula")

def main():
    args = AP.parse_args()
    print(args)

if __name__ == "__main__":
    main()