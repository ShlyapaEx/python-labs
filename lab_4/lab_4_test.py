import pytest
import smtplib

pytest.global_counter = 1


@pytest.fixture(autouse=True)
def annoying_screamer():
    print(f"Надел мужик шляпу, а она ему как {pytest.global_counter}")
    pytest.global_counter += 1


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.xfail
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


@pytest.mark.parametrize("test_value,expected", [(1, 1), (10, 100), (3, 9)])
def test_eval(test_value, expected):
    print(test_value, expected)
    assert test_value ** 2 == expected


@pytest.fixture(scope="module")
def get_smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection  # возвращает значение фикстуры
    print("teardown smtp")
    smtp_connection.close()


def test_with_fixture(get_smtp_connection: smtplib.SMTP):
    print(get_smtp_connection)
    assert isinstance(get_smtp_connection, smtplib.SMTP)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


@pytest.mark.special
def test_special():
    print("Я особенный :)")


@pytest.mark.skip
def test_skip_protivnyi():
    print("Меня никто не любит :c")
