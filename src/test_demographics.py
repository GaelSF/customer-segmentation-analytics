from generators.demographics import (
    generate_gender,
    generate_age,
    generate_state,
    generate_city
)


for _ in range(10):

    state = generate_state()

    print(
        {
            "gender": generate_gender(),
            "age": generate_age(),
            "state": state,
            "city": generate_city(state)
        }
    )