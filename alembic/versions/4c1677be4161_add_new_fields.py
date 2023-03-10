"""Add new fields

Revision ID: 4c1677be4161
Revises: 33aa0e51df5f
Create Date: 2023-02-07 16:48:13.983554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c1677be4161'
down_revision = '33aa0e51df5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('places', sa.Column('host_name', sa.String(length=100), nullable=True))
    op.add_column('places', sa.Column('host_phone', sa.String(length=100), nullable=True))
    op.add_column('places', sa.Column('host_location', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('places', 'host_location')
    op.drop_column('places', 'host_phone')
    op.drop_column('places', 'host_name')
    # ### end Alembic commands ###
