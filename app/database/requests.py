from app.database.models import async_session
from app.database.models import SurveyResponse

async def save_survey_data(user_id: int, name: str, number: str, anime: str, book: str):
    async with async_session() as session:
        new_survey = SurveyResponse(user_id=user_id, name=name, number=number, anime=anime, book=book)
        session.add(new_survey)
        await session.commit()
