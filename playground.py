from datetime import date
import inflect

def total(start, now):
    end = (now - start).days * 24 * 60
    return end

def main():
    try:
        start = input("Start date: ")
    except ValueError:
        sys.exit(3)
    start = data.formisoformat(start)
    ili = date.today()
    mins = total(start, ili)

    p = inflect.engine()
    thing = p.number_to_words(mins, andword='')
    thing_p = p.plural('minute', mins)
    print(f'{thing} {thing_p}')





if __name__ == "__main__":
    main()
