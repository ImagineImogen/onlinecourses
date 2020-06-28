import graphene
from courses.schema import Query as QueryGraphQL

class Query(QueryGraphQL, graphene.ObjectType): #coursespro.courses.schema.Query
    pass

schema = graphene.Schema(query=Query)