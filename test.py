import mcp
import pkgutil
if __name__ == '__main__':
    for m in pkgutil.walk_packages(mcp.__path__, mcp.__name__ + "."):
        print(m.name)