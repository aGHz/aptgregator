"""Create listings table

Revision ID: 46837b9824a
Revises: None
Create Date: 2014-04-03 21:50:39.639237

"""

# revision identifiers, used by Alembic.
revision = '46837b9824a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=50), nullable=True),
    sa.Column('title', sa.Unicode(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.Column('price', sa.Float(asdecimal=True), nullable=True),
    sa.Column('has_image', sa.Boolean(), nullable=True),
    sa.Column('posted_on', sa.DateTime(), nullable=True),
    sa.Column('map_url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('listing')
    ### end Alembic commands ###
