"""empty message

Revision ID: b0fc67a096fe
Revises: 0d8662dfb68a
Create Date: 2021-05-05 14:24:03.870443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String


# revision identifiers, used by Alembic.
revision = 'b0fc67a096fe'
down_revision = '0d8662dfb68a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('searchColumns', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###
    states_table = table(
        'states',
        column('cd', String),
        column('description', String)
    )
    try:
        op.bulk_insert(
            states_table,
            [
                {
                    'cd': 'PENDING_PAYMENT',
                    'description': 'NR has been created, but payment is not completed yet'
                }
            ]
        )
    except IntegrityError:
        pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'searchColumns')
    # ### end Alembic commands ###
