from app.util import BaseService, IUnitOfWork, send_mail_to_verify_user
from app.schemas import UserCreate
from passlib.hash import pbkdf2_sha256

class UserService(BaseService):

    repository = 'user'

    async def create(self, data: UserCreate, uow: IUnitOfWork):
        async with uow:
            data.password = pbkdf2_sha256.hash(data.password)
            data_dict = data.model_dump()
            user = await uow.user.create(data_dict)
            if user is not None:
                send_mail_to_verify_user(user)
            await uow.commit()
            return user
        
    
