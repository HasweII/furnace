from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List

from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine
from .models.category import Category
from .models.product import Product


@dataclass(frozen=True)
class FurnacePayload:
    furnace_id: int
    furnace_name: str
    furnace_info: str
    furnace_type: str
    image_res: str


FURNACES: List[FurnacePayload] = [
    FurnacePayload(
        furnace_id=1,
        furnace_name="Доменная печь",
        furnace_info="Восстановительная плавка железорудного сырья с коксом для получения чугуна; основа классической связки BF-BOF.",
        furnace_type="черная",
        image_res="img_bf",
    ),
    FurnacePayload(
        furnace_id=2,
        furnace_name="Кислородный конвертер (BOF/LD)",
        furnace_info="Передел жидкого чугуна в сталь кислородной продувкой; быстрый массовый процесс.",
        furnace_type="черная",
        image_res="img_bof",
    ),
    FurnacePayload(
        furnace_id=3,
        furnace_name="Электродуговая печь (ДСП/EAF)",
        furnace_info="Плавка стального лома или DRI электрической дугой; гибкая и подходящая для декарбонизации.",
        furnace_type="черная",
        image_res="img_eaf",
    ),
    FurnacePayload(
        furnace_id=4,
        furnace_name="Индукционная печь",
        furnace_info="Переплав и получение сплавов индукционным нагревом; чистая плавка, чаще для цветных и мелкосерийной стали.",
        furnace_type="цветная",
        image_res="img_if",
    ),
    FurnacePayload(
        furnace_id=5,
        furnace_name="Ковш-печь (LF)",
        furnace_info="Доводка состава и температуры стали под шлаком, рафинирование и десульфурация.",
        furnace_type="черная",
        image_res="img_lf",
    ),
    FurnacePayload(
        furnace_id=6,
        furnace_name="Вакуумная дегазация (VD)",
        furnace_info="Удаление водорода/азота/кислорода из стали под вакуумом для повышения чистоты.",
        furnace_type="черная",
        image_res="img_vd",
    ),
    FurnacePayload(
        furnace_id=7,
        furnace_name="Вакуум-кислородная рафинация (VOD)",
        furnace_info="Деуглероживание нержавеющей стали под вакуумом с подачей O2; очень низкий C.",
        furnace_type="черная",
        image_res="img_vod",
    ),
    FurnacePayload(
        furnace_id=8,
        furnace_name="Вращающаяся печь RKEF (латериты)",
        furnace_info="Сушка/кальцинация/частичное восстановление никелевых латеритов перед SAF в схеме RKEF.",
        furnace_type="цветная",
        image_res="img_rkef_kiln",
    ),
    FurnacePayload(
        furnace_id=9,
        furnace_name="Подводно-дуговая электропечь (SAF)",
        furnace_info="Глубокое восстановление под шлаком для ферросплавов, меди/никеля и др.; высокая мощность.",
        furnace_type="черная",
        image_res="img_saf",
    ),
    FurnacePayload(
        furnace_id=10,
        furnace_name="Флэш-плавка",
        furnace_info="Плавка сульфидных концентратов Cu/Ni в пылевом потоке с кислородом; энергоэффективна, SO₂ утилизируется.",
        furnace_type="цветная",
        image_res="img_flash",
    ),
    FurnacePayload(
        furnace_id=11,
        furnace_name="Печь с погружной фурмой (TSL)",
        furnace_info="Интенсивная плавка концентратов и пылей с кислородом (Ausmelt/Isasmelt); гибкий режим.",
        furnace_type="цветная",
        image_res="img_tsl",
    ),
    FurnacePayload(
        furnace_id=12,
        furnace_name="Конвертер Пирса–Смита",
        furnace_info="Конвертирование медного/никелевого штейна в блистер под боковой продувкой.",
        furnace_type="цветная",
        image_res="img_pierce_smith",
    ),
    FurnacePayload(
        furnace_id=13,
        furnace_name="Анодная печь",
        furnace_info="Рафинирование блистерной меди до анодной перед электролизом; режимы окисление/полировка.",
        furnace_type="цветная",
        image_res="img_anode_furnace",
    ),
    FurnacePayload(
        furnace_id=14,
        furnace_name="Ваэльц-печь",
        furnace_info="Возврат цинка/свинца из металлургических пылей во вращающейся печи при восстановлении.",
        furnace_type="цветная",
        image_res="img_waelz",
    ),
    FurnacePayload(
        furnace_id=15,
        furnace_name="КИВЦЭТ",
        furnace_info="Комбинированный обжиг и плавка свинцовых/цинковых концентратов с кислородом; замкнутая газоочистка.",
        furnace_type="цветная",
        image_res="img_kivcet",
    ),
    FurnacePayload(
        furnace_id=16,
        furnace_name="Печь Imperial Smelting (ISF)",
        furnace_info="Совместная восстановительная плавка Pb+Zn с последующей конденсацией паров цинка.",
        furnace_type="цветная",
        image_res="img_isf",
    ),
    FurnacePayload(
        furnace_id=17,
        furnace_name="Кальцинатор в кипящем слое",
        furnace_info="Кальцинация гидроксида алюминия до глинозёма в (циркулирующем) кипящем слое; высокий КПД.",
        furnace_type="цветная",
        image_res="img_fb_calciner",
    ),
    FurnacePayload(
        furnace_id=18,
        furnace_name="Вращающаяся печь (кальцинация)",
        furnace_info="Обжиг/кальцинация Al(OH)₃ или известняка в барабанной печи; универсальна, но менее экономична vs FBC.",
        furnace_type="цветная",
        image_res="img_rotary_kiln",
    ),
    FurnacePayload(
        furnace_id=19,
        furnace_name="Отражательная печь",
        furnace_info="Газопламенная ванновая плавка (исторически для меди/лома); сегодня вытеснена более эффективными схемами.",
        furnace_type="цветная",
        image_res="img_reverb",
    ),
    FurnacePayload(
        furnace_id=20,
        furnace_name="TBRC/Kaldo",
        furnace_info="Кислородно-конвертерная вращающаяся печь для рафинирования штейнов и металлов цветной металлургии.",
        furnace_type="цветная",
        image_res="img_tbrc",
    ),
    FurnacePayload(
        furnace_id=21,
        furnace_name="Шагоходная нагревательная печь",
        furnace_info="Нагрев слитков/слябов перед горячей прокаткой; равномерный профиль температуры.",
        furnace_type="черная",
        image_res="img_walking_beam",
    ),
    FurnacePayload(
        furnace_id=22,
        furnace_name="VIM (вакуумно-индукционная плавка)",
        furnace_info="Плавка высоколегированных/реактивных сплавов в вакууме с индукционным нагревом.",
        furnace_type="черная",
        image_res="img_vim",
    ),
    FurnacePayload(
        furnace_id=23,
        furnace_name="Электронно-лучевая печь (EB)",
        furnace_info="Высокочистая плавка титана/редких металлов электронным лучом в глубоком вакууме.",
        furnace_type="цветная",
        image_res="img_eb",
    ),
    FurnacePayload(
        furnace_id=24,
        furnace_name="Известковая печь",
        furnace_info="Обжиг известняка до CaO для флюсования и металлургии; значимые выбросы CO₂.",
        furnace_type="черная",
        image_res="img_lime_kiln",
    ),
]


TRANSLIT_MAP: Dict[str, str] = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def slugify(value: str) -> str:
    """Convert Cyrillic text to a simple ASCII slug."""
    value = value.strip().lower()
    transliterated = "".join(TRANSLIT_MAP.get(char, char) for char in value)
    safe = []
    for char in transliterated:
        if char.isalnum():
            safe.append(char)
        elif char in {" ", "-", "_"}:
            safe.append("-")
    slug = "".join(safe).strip("-")
    return slug or "category"


def ensure_categories(session: Session, furnace_rows: Iterable[FurnacePayload]) -> Dict[str, Category]:
    """Create missing categories derived from furnace types."""
    categories: Dict[str, Category] = {}
    for payload in furnace_rows:
        raw_name = payload.furnace_type.strip()
        category_name = raw_name.capitalize()
        slug = slugify(raw_name)

        if category_name in categories:
            continue

        existing = session.query(Category).filter_by(slug=slug).first()
        if existing:
            categories[category_name] = existing
            continue

        category = Category(name=category_name, slug=slug)
        session.add(category)
        session.flush()
        categories[category_name] = category

    return categories


def ensure_products(session: Session, furnace_rows: Iterable[FurnacePayload], categories: Dict[str, Category]) -> None:
    """Insert furnaces as products linked to the seeded categories."""
    for payload in furnace_rows:
        if session.query(Product).filter_by(name=payload.furnace_name).first():
            continue

        category_key = payload.furnace_type.strip().capitalize()
        category = categories[category_key]
        product = Product(
            name=payload.furnace_name,
            description=payload.furnace_info,
            category_id=category.id,
            image_url=f"/static/images/{payload.image_res}.jpg",
        )
        session.add(product)


def seed() -> None:
    """Populate the database with initial categories and products."""
    Base.metadata.create_all(bind=engine)

    session: Session = SessionLocal()
    try:
        categories = ensure_categories(session, FURNACES)
        ensure_products(session, FURNACES, categories)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed()
