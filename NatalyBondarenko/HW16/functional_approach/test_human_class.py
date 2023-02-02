import faker
import pytest
import random


@pytest.mark.create_human
@pytest.mark.parametrize("age, gender", [(random.randint(1, 99), "female"), (random.randint(1, 99), "male")],
                         ids=['create female human', 'create male human'])
def test_create_human(create_custom_human_instance, age, gender):
    name = faker.name()
    human = create_custom_human_instance(name, age, gender)
    assert human._Human__name == name, (f'Incorrect name'
                                        f'\nActual: {human.name}'
                                        f'\nExpected: {name}')

    assert human.age == age, (f'Incorrect age'
                              f'\nActual: {human.age}'
                              f'\nExpected: {age}')

    assert human.gender == gender, (f'Incorrect gender'
                                    f'\nActual: {human.gender}'
                                    f'\nExpected: {gender}')


@pytest.mark.negative
@pytest.mark.skip(reason='Name value validation need to be added')
def test_invalid_name_int(create_invalid_human_name_int):
    with pytest.raises(ValueError, match="Value for parameter name - can not be int"):
        human = create_invalid_human_name_int


@pytest.mark.negative
@pytest.mark.skip(reason='Name value validation need to be added')
def test_invalid_name_empty_value(create_invalid_human_name_empty):
    with pytest.raises(ValueError, match="Value for parameter 'name' - can not be empty"):
        human = create_invalid_human_name_empty


@pytest.mark.invalid_gender
def test_error_on_invalid_gender(create_custom_human_instance, faker):
    human = create_custom_human_instance(faker.name(), random.randint(1, 99), "female")
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender('ledyboy')


@pytest.mark.invalid_gender
def test_error_on_change_gender_to_the_same_value(create_custom_human_instance):
    human = create_custom_human_instance(faker.name(), random.randint(1, 99), 'male')
    gender = human.gender
    with pytest.raises(Exception, match=f"{human._Human__name} already has gender '{gender}'"):
        human.change_gender('male')


@pytest.mark.change_gender
@pytest.mark.parametrize("gender, new_gender", [("male", "female"), ("female", "male")],
                         ids=["female to male", "male to female"])
def test_change_gender(create_custom_human_instance, faker, gender, new_gender):
    human = create_custom_human_instance(faker.name(), random.randint(1, 99), gender)
    human.change_gender(new_gender)

    assert human.gender == new_gender, (f'Gender was not chanced'
                                        f'\nActual: {gender}'
                                        f'\nExpected: {new_gender}')


@pytest.mark.human_grow
def test_human_grow(create_custom_human_instance, faker):
    human = create_custom_human_instance(faker.name(), random.randint(1, 99), 'female')
    age = human.age
    human.grow()

    assert human.age == age + 1, (f'{human._Human__name} age was not chanced'
                                  f'\nActual: {age}'
                                  f'\nExpected: {age + 1}')

    assert human._Human__is_alive, (f'Human status is not correct'
                                    f'\nActual: {human._Human__status}'
                                    f'\nExpected: alive')


@pytest.mark.negative
@pytest.mark.skip(reason='Validation for parameter "age" needs to be added')
def test_invalid_age_negative(create_invalid_human_age_negative):
    with pytest.raises(ValueError, match="Value for parameter age - can not be less than 0"):
        human = create_invalid_human_age_negative


@pytest.mark.negative
@pytest.mark.skip(reason='Validation for parameter "age" needs to be added')
def test_invalid_age_str(create_invalid_human_age_str):
    with pytest.raises(ValueError, match="Value for parameter age - can not be str"):
        human = create_invalid_human_age_str


@pytest.mark.dead
def test_error_dead_status(create_custom_human_instance, faker):
    age = random.randint(100, 105)
    human = create_custom_human_instance(faker.name(), age, 'female')
    human.grow()

    assert human._Human__status == "dead", (f'Human status is incorrect'
                                            f'\nActual: {human._Human__status}'
                                            f'\nExpected: dead')

    assert human.age == age, f' {human.age} is unsupported value'

    with pytest.raises(Exception, match=f"{human._Human__name} is already dead..."):
        human._Human__is_alive()
