import logging
import less11

def main():
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)
# INFO LEVEL COVERS WARNING AND ERROR SO USE THIS ONE
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("Program started")
    result = less11.print_data()
    logger.info("Done!")


if __name__ == "__main__":
    main()