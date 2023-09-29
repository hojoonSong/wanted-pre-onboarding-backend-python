from django.core.management.base import BaseCommand
from ...models import Company


class Command(BaseCommand):
    help = "임의의 회사 20개를 추가합니다."

    def handle(self, *args, **kwargs):
        companies = [
            {"name": "삼성전자", "country": "대한민국", "region": "경기도 수원시"},
            {"name": "카카오", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "네이버", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "SK하이닉스", "country": "대한민국", "region": "경기도 이천시"},
            {"name": "LG전자", "country": "대한민국", "region": "서울특별시 영등포구"},
            {"name": "삼성SDS", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "KT", "country": "대한민국", "region": "서울특별시 성동구"},
            {"name": "LG CNS", "country": "대한민국", "region": "서울특별시 영등포구"},
            {"name": "NC소프트", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "넥슨", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "CJ ENM", "country": "대한민국", "region": "서울특별시 상암동"},
            {"name": "두산그룹", "country": "대한민국", "region": "서울특별시 중구"},
            {"name": "한화시스템", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "카카오게임즈", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "컴투스", "country": "대한민국", "region": "서울특별시 송파구"},
            {"name": "아프리카TV", "country": "대한민국", "region": "경기도 성남시"},
            {"name": "넷마블", "country": "대한민국", "region": "서울특별시 광진구"},
            {"name": "웹젠", "country": "대한민국", "region": "서울특별시 마포구"},
            {"name": "펍지", "country": "대한민국", "region": "서울특별시 강남구"},
            {"name": "크래프톤", "country": "대한민국", "region": "서울특별시 성동구"},
        ]

        for company in companies:
            Company.objects.create(**company)
            self.stdout.write(self.style.SUCCESS(f"Successfully added company {company['name']}"))
