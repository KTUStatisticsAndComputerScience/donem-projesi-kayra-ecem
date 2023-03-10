"""empty message

Revision ID: f8c95d6f2ae3
Revises: 
Create Date: 2022-12-16 10:18:33.057185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c95d6f2ae3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kisi',
    sa.Column('kisi_id', sa.Integer(), nullable=False),
    sa.Column('kisi_adi', sa.String(length=255), nullable=True),
    sa.Column('kisi_soyadi', sa.String(length=255), nullable=True),
    sa.Column('tel', sa.String(length=12), nullable=True),
    sa.Column('adres', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('kisi_id')
    )
    op.create_table('sehir',
    sa.Column('sehir_id', sa.Integer(), nullable=False),
    sa.Column('sehir_adi', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('sehir_id')
    )
    op.create_table('kargo',
    sa.Column('kargo_id', sa.Integer(), nullable=False),
    sa.Column('kargo_adi', sa.String(length=255), nullable=True),
    sa.Column('alici', sa.Integer(), nullable=True),
    sa.Column('gonderici', sa.Integer(), nullable=True),
    sa.Column('agirlik', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alici'], ['kisi.kisi_id'], ),
    sa.ForeignKeyConstraint(['gonderici'], ['kisi.kisi_id'], ),
    sa.PrimaryKeyConstraint('kargo_id')
    )
    op.create_table('sube',
    sa.Column('sube_id', sa.Integer(), nullable=False),
    sa.Column('sube_sehiri', sa.Integer(), nullable=True),
    sa.Column('sube_adi', sa.String(length=255), nullable=True),
    sa.Column('sube_tel', sa.String(length=12), nullable=True),
    sa.ForeignKeyConstraint(['sube_sehiri'], ['sehir.sehir_id'], ),
    sa.PrimaryKeyConstraint('sube_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sube')
    op.drop_table('kargo')
    op.drop_table('sehir')
    op.drop_table('kisi')
    # ### end Alembic commands ###
