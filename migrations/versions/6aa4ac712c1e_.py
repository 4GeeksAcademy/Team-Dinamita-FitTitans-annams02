"""empty message

Revision ID: 6aa4ac712c1e
Revises: 3b5f7f3f9a78
Create Date: 2024-05-29 18:44:07.826627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa4ac712c1e'
down_revision = '3b5f7f3f9a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('telefono', sa.String(length=80), nullable=False))
        batch_op.drop_constraint('user_phone_key', type_='unique')
        batch_op.drop_constraint('user_username_key', type_='unique')
        batch_op.create_unique_constraint(None, ['nombre'])
        batch_op.create_unique_constraint(None, ['telefono'])
        batch_op.drop_column('phone')
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('phone', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_username_key', ['username'])
        batch_op.create_unique_constraint('user_phone_key', ['phone'])
        batch_op.drop_column('telefono')
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###