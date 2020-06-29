import graphene
from courses.schema import Query as QueryGraphQL
from courses.schema import Mutation as MutationGraphQL

class Query(QueryGraphQL, graphene.ObjectType): #coursespro.courses.schema.Query
    pass

class Mutation(MutationGraphQL, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)