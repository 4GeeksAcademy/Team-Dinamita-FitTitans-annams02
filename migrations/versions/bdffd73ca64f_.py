"""empty message

<<<<<<< HEAD:migrations/versions/bdffd73ca64f_.py
Revision ID: bdffd73ca64f
Revises: 
Create Date: 2024-06-12 15:34:47.604960
=======
Revision ID: 25213e1c220c
Revises: 
Create Date: 2024-06-11 19:35:42.707272
>>>>>>> d044c849c1c117b2e27606b5d929df2dc97b2970:migrations/versions/25213e1c220c_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:migrations/versions/bdffd73ca64f_.py
revision = 'bdffd73ca64f'
=======
revision = '25213e1c220c'
>>>>>>> d044c849c1c117b2e27606b5d929df2dc97b2970:migrations/versions/25213e1c220c_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('rol', sa.Boolean(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.String(length=120), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('genero', sa.String(length=10), nullable=True),
    sa.Column('altura', sa.String(length=30), nullable=True),
    sa.Column('tipo_entrenamiento', sa.String(length=100), nullable=True),
    sa.Column('foto', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telefono')
    )
    op.create_table('asignacion_entrenador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entrenador_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('dieta', sa.String(length=100), nullable=True),
    sa.Column('rutina', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['entrenador_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('asignacion_entrenador')
    op.drop_table('user')
    # ### end Alembic commands ###