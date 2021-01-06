#include <iostream>

using namespace std;

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
} *r;

class AVLTree{
    public:
        AVLTree(){ r = NULL;}
        int hight(Node *);
        int difference(Node *);
        Node* ll_rotation(Node*);
        Node* rr_rotation(Node*);
        Node* rl_rotation(Node*);
        Node* lr_rotation(Node*);
        Node* balance(Node*);
        Node* insert(Node*, int);
        void in_order(Node*);
        void pre_order(Node*);
        void post_order(Node*);
};

int AVLTree::hight(Node* temp)
{
    int h = 0;
    if(temp != NULL){
        int left_hight = AVLTree::hight(temp->left);
        int right_hight = AVLTree::hight(temp->right);
        int max_hight = max(left_hight,right_hight);
        h = max_hight + 1;
    
    return h;
}

int AVLTree::difference (Node *temp){
    int left_hight = AVLTree::hight(temp->left);
    int right_hight = AVLTree::hight(temp->right);
    int b_factor = left_hight - right_hight;
    return b_factor;

}


Node *AVLTree::rr_rotation(Node* parent)
{
    Node* temp = parent->left;
    parent->left = temp->right;
    temp->right = parent;
    cout << "Left-Left Rotation\n";
    return temp;
}

Node* AVLTree::ll_rotation(Node* parent)
{
    Node* temp = parent->right;
    parent->right = temp->left;
    temp->left = parent;
    cout << "Right-Right Rotation\n";
    return temp;
}

Node* AVLTree::lr_rotation(Node* parent)
{
    Node* temp = parent->left;
    parent->left = rr_rotation(temp);
    cout << "Left-Right Rotation";
    return AVLTree::ll_rotation(parent);
}

Node* AVLTree::rl_rotation(Node* parent)
{
    Node* temp = parent->right;
    parent->right = ll_rotation(temp);
    cout << "Right-Left Rotation\n";
    return rr_rotation(parent); 
}

Node* AVLTree::balance(Node* temp)
{
    int factor = difference(temp);
    if(factor > 1){
        if(difference(temp->right) > 0)
            temp = ll_rotation(temp);
        else
            temp = lr_rotation(temp);
    }
    else if (factor < -1){
        if(difference(temp->right) > 0)
            temp = rr_rotation(temp);
        else
            temp = rl_rotation(temp);
    }
    return temp;
}

Node* AVLTree::insert(Node* root, int value)
{
    if(root == NULL){
        root = new Node;
        root->data = value;
        root->left = NULL;
        root->right = NULL;
    }
    else if (root->data >= value){
        root->right = insert(root->right, value);
        root = balance(root);
    }
    else if(root->data < value){
        root->left = insert(root->left, value);
        root = balance(root);
    }

    return root;
    
}

void AVLTree::in_order(Node* temp)
{
    if(temp == NULL)
        return;
    in_order(temp->left);
    cout << temp->data << " , ";
    in_order(temp->right);
}
void AVLTree::pre_order(Node* temp)
{
    if(temp == NULL)
        return;
    cout << temp->data << " , ";
    pre_order(temp->left);
    pre_order(temp->right);
}
void AVLTree::post_order(Node* temp)
{
    if(temp == NULL)
        return;
    post_order(temp->left);
    post_order(temp->right);
    cout << temp->data << " , ";
}
int main()
{
    int choice;
    int value;
    avltree avl;
    while (1){
        cout <<"\n\n---------------------------------------------\n\n";
        cout << "1.Insert Element into the tree" << endl;
        cout << "2.show Balanced AVL Tree" << endl;
        cout << "3.InOrder traversal" << endl;
        cout << "4.PreOrder traversal" << endl;
        cout << "5.PostOrder traversal" << endl;
        cout << "6.Exit" << endl;
        cout << "Enter your Choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "Enter value to be inserted.";
            cin >> value;
            r = avl.insert() 
            break;
        case 3:
            avl.in_order(r); 
        default:
            break;
        }
        // switch (choice){
        //     case 1:
        //         cout << "Enter value to be inserted: ";
        //         cin >> value;
        //         //r = avl.insert(r,value);
        //         break;
        //     case 3:
        //         //avl.in_order(r);
        //         cout << endl;
        //         break;
            
        //     // case 4:
        //     //     avl.pre_order(r);
        //     //     break;
        //     // case 5:
        //     //     avl.post_order(r);
        //     //     break;
        //     // case 6:
        //     //     exit(1);
        //     //     break;
        //     // default:
        //     //     cout << "Wrong Choice.";
        //     //     break;
        // }
    }
    //return 0; 
}