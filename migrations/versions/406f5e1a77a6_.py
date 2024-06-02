"""empty message

Revision ID: 406f5e1a77a6
Revises: bd0648011695
Create Date: 2024-05-29 19:57:00.411670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '406f5e1a77a6'
down_revision = 'bd0648011695'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('telefono', sa.String(length=80), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.alter_column('is_trainer',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['telefono'])
        batch_op.create_unique_constraint(None, ['nombre'])
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('is_trainer',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('telefono')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###