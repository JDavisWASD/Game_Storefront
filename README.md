# Read Me!

Documentation:
  Friends class:
    get_all_by_user(data):
      data needs to have user_id
      returns a list of User objects
    get_one_by_ids(data):
      data needs to have user_id and friend_id
      returns a single Friend object
    save(data):
      data needs to have user_id and friend_id
      returns row id
    delete(data):
      data needs to have user_id and friend_id
