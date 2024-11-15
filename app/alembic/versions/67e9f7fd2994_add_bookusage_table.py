"""Add BookUsage table

Revision ID: 67e9f7fd2994
Revises: 324a4e4d2260
Create Date: 2024-11-11 20:32:13.711777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67e9f7fd2994'
down_revision: Union[str, None] = '324a4e4d2260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_usages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('date_borrowed', sa.DateTime(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('date_returned', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_usages_id'), 'book_usages', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_usages_id'), table_name='book_usages')
    op.drop_table('book_usages')
    # ### end Alembic commands ###
